import asyncio
import logging
from asyncio import AbstractEventLoop
from datetime import datetime
from typing import *

from faker import Faker
from outcache import CacheAsync

from .errors import PyBeatSaverException
from .beatsaver_provider import BeatSaverProvider
from .http_client import HttpClient
from .models import MapDetail, EMapSort, ESearchAutoMapper, ESearchSortOrder, SearchResponse, UserDetail, EMapTag


class BeatSaver:
    TIMEOUT = 10
    _url = "https://api.beatsaver.com"

    def __init__(self, loop: Optional[AbstractEventLoop] = None, test_mode: bool = False):
        self.loop = loop if loop is not None else asyncio.get_event_loop()
        self.test_mode = test_mode

        self.log = logging.getLogger(__name__)
        self._http_client = HttpClient(self.loop)

        if test_mode:
            self.faker = Faker()
            Faker.seed(76561198283584459)
            self.faker.add_provider(BeatSaverProvider)

    async def start(self):
        await self._http_client.start()

    async def close(self):
        await self._http_client.close()

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    # /maps

    @CacheAsync(hours=1)
    async def beatmap(self,
        beatmap_key: str
    ) -> MapDetail:
        if self.test_mode:
            return self.faker.map_detail(beatmap_key=beatmap_key)

        return await self._http_client.get(MapDetail, f"{self._url}/maps/id/{beatmap_key}")

    @CacheAsync(hours=1)
    async def beatmap_by_hash(self,
        beatmap_hash: str
    ) -> MapDetail:
        if self.test_mode:
            return self.faker.map_detail(beatmap_hash=beatmap_hash)

        map_detail = await self._http_client.get(MapDetail, f"{self._url}/maps/hash/{beatmap_hash}")

        for map_version in map_detail.versions:
            if map_version.hash == beatmap_hash:
                return map_detail

        raise PyBeatSaverException(f"Found beatmap with wrong hash! {beatmap_hash} != {map_detail.versions[0].hash}")

    @CacheAsync(hours=1)
    async def beatmaps_by_hashes(self,
        beatmap_hashes: List[str]
    ) -> List[MapDetail]:
        if self.test_mode:
            return self.faker.map_details_by_hash(beatmap_hashes)

        if len(beatmap_hashes) > 50:
            raise PyBeatSaverException("You can only get 50 hashes at a time!")

        data = await self._http_client.get_raw(f"{self._url}/maps/hash/{','.join(beatmap_hashes)}")

        # We got a single beatmap back
        if data.get("id") is not None:
            return [MapDetail.from_dict(data)]

        beatmaps = []

        for beatmap_hash in beatmap_hashes:
            # If the hash is not found it will return a None.
            if beatmap_hash in data and data[beatmap_hash] is not None:
                map_detail = MapDetail.from_dict(data[beatmap_hash])

                # Check if the hash produced a version with same hash.
                # There are hashes that point to a different hashed version.
                for map_version in map_detail.versions:
                    if map_version.hash == beatmap_hash:
                        beatmaps.append(map_detail)
                        break

        return beatmaps

    @CacheAsync(minutes=5)
    async def user_beatmaps(self,
        user_id: int,
        page: int = 0
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise PyBeatSaverException("Running in test mode")

            return self.faker.map_details(100, uploader_id=user_id)

        search_response = await self._http_client.get(SearchResponse, f"{self._url}/maps/uploader/{user_id}/{page}")
        return search_response.docs

    @CacheAsync(minutes=1)
    async def latest_beatmaps(self,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        auto_mapper: Optional[bool] = None,
        sort_by: Optional[EMapSort] = None
    ) -> List[MapDetail]:
        if self.test_mode:
            return self.faker.map_details(100)

        params = {
            "before": before, "after": after, "automapper": auto_mapper,
            "sort": sort_by
        }

        search_response = await self._http_client.get(SearchResponse, f"{self._url}/maps/latest", params)
        return search_response.docs

    @CacheAsync(hours=24)
    async def beatmaps_ordered_by_plays(self,
        page: int = 0
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise PyBeatSaverException("Running in test mode")

            return self.faker.map_details(100)

        search_response = await self._http_client.get(SearchResponse, f"{self._url}/maps/plays/{page}")
        return search_response.docs

    # /users
    @CacheAsync(hours=24)
    async def user(self,
        user_id: int
    ) -> UserDetail:
        if self.test_mode:
            return self.faker.user_detail(user_id=user_id)

        return await self._http_client.get(UserDetail, f"{self._url}/users/id/{user_id}")

    @CacheAsync(hours=24)
    async def user_by_username(self,
        username: str
    ) -> UserDetail:
        if self.test_mode:
            return self.faker.user_detail(username=username)

        return await self._http_client.get(UserDetail, f"{self._url}/users/name/{username}")

    # TODO: Implement POST /users/verify

    # /search

    @CacheAsync(hours=1)
    async def search_beatmaps(self,
        search_query: Optional[str] = None,
        max_bpm: Optional[float] = None,
        max_duration: Optional[int] = None,
        max_nps: Optional[float] = None,
        max_rating: Optional[float] = None,
        min_bpm: Optional[float] = None,
        min_duration: Optional[int] = None,
        min_nps: Optional[float] = None,
        min_rating: Optional[float] = None,
        noodle: Optional[bool] = None,
        me: Optional[bool] = None,
        chroma: Optional[bool] = None,
        cinema: Optional[bool] = None,
        ranked: Optional[bool] = None,
        full_spread: Optional[bool] = None,
        curated: Optional[bool] = None,
        auto_mapper: Optional[ESearchAutoMapper] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        sort_order: Optional[ESearchSortOrder] = ESearchSortOrder.LATEST,
        tags: Optional[List[EMapTag]] = None,
        page: int = 0,
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise PyBeatSaverException("Running in test mode")

            logging.warning(f"search_beatmaps is returning random maps")

            return self.faker.map_details(100)

        params = {
            "q": search_query, "maxBpm": max_bpm, "maxDuration": max_duration,
            "maxNps": max_nps, "maxRating": max_rating, "minBpm": min_bpm,
            "minDuration": min_duration, "minNps": min_nps, "minRating": min_rating,
            "noodle": noodle, "me": me, "chroma": chroma, "cinema": cinema,
            "ranked": ranked, "full_spread": full_spread, "automapper": auto_mapper,
            "from": from_date, "to": to_date, "sortOrder": sort_order, "curated": curated,
            "tags": tags
        }

        search_response = await self._http_client.get(SearchResponse, f"{self._url}/search/text/{page}", params)
        return search_response.docs
    # /vote

    # TODO: Implement GET /vote

    # TODO: Implement POST /vote

    # /playlists

    # TODO: Implement GET /playlists/latest
    # TODO: Implement GET /playlists/search/{page}
    # TODO: Implement GET /playlists/id/{id}/{page}
    # TODO: Implement GET /playlists/user/{userId}/{page}
