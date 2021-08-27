import asyncio
import logging
from asyncio import AbstractEventLoop
from datetime import datetime
from typing import *

from faker import Faker
from outcache import CacheAsync

from .errors import BeatSaverException
from .beatsaver_provider import BeatSaverProvider
from .http_client import HttpClient
from .models import MapDetail, MapSort, SearchAutoMapper, SearchSortOrder, SearchResponse, UserDetail


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

        return await self._http_client.get(MapDetail, f"{self._url}/maps/hash/{beatmap_hash}")

    @CacheAsync(hours=1)
    async def beatmaps_by_hashes(self,
        beatmap_hashes: List[str]
    ) -> List[MapDetail]:
        if self.test_mode:
            return self.faker.map_details_by_hash(beatmap_hashes)

        if len(beatmap_hashes) > 50:
            raise ValueError("You can only get 50 hashes at a time!")

        data = await self._http_client.get_reg(f"{self._url}/maps/hash/{','.join(beatmap_hashes)}")

        beatmaps = []

        for beatmap_hash in beatmap_hashes:
            beatmaps.append(MapDetail.from_dict(data[beatmap_hash]))

        return beatmaps

    @CacheAsync(minutes=5)
    async def user_beatmaps(self,
        user_id: int,
        page: int = 0
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise BeatSaverException(404, "Running in test mode")

            return self.faker.map_details(100, uploader_id=user_id)

        search_response = await self._http_client.get(SearchResponse, f"{self._url}/maps/uploader/{user_id}/{page}")
        return search_response.docs

    @CacheAsync(minutes=1)
    async def latest_beatmaps(self,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        auto_mapper: Optional[bool] = None,
        sort_by: Optional[MapSort] = None
    ) -> List[MapDetail]:
        if self.test_mode:
            beatmaps = []

            return self.faker.map_details(100)

        query = f"{self._url}/maps/latest"
        params = []

        if before is not None:
            params.append(f"before={before}")

        if after is not None:
            params.append(f"after={after}")

        if auto_mapper is not None:
            params.append(f"automapper={auto_mapper}")

        if sort_by is not None:
            params.append(f"sort={sort_by}")

        if len(params) > 0:
            query += "?" + "&".join(params)

        search_response = await self._http_client.get(SearchResponse, query)
        return search_response.docs

    @CacheAsync(hours=24)
    async def beatmaps_ordered_by_plays(self,
        page: int = 0
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise BeatSaverException(404, "Running in test mode")

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
        search_question: Optional[str] = None,
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
        auto_mapper: Optional[SearchAutoMapper] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        sort_order: Optional[SearchSortOrder] = SearchSortOrder.LATEST,
        page: int = 0,
    ) -> List[MapDetail]:
        if self.test_mode:
            if page > 1:
                raise BeatSaverException(404, "Running in test mode")

            logging.warning(f"search_beatmaps is returning random maps")

            return self.faker.map_details(100)

        query = f"{self._url}/search/text/{page}"
        params = []

        if search_question is not None:
            params.append(f"q={search_question}")

        if max_bpm is not None:
            params.append(f"maxBpm={max_bpm}")

        if max_duration is not None:
            params.append(f"maxDuration={max_duration}")

        if max_nps is not None:
            params.append(f"maxNps={max_nps}")

        if max_rating is not None:
            params.append(f"maxRating={max_rating}")

        if min_bpm is not None:
            params.append(f"minBpm={min_bpm}")

        if min_duration is not None:
            params.append(f"minDuration={min_duration}")

        if min_nps is not None:
            params.append(f"minNps={min_nps}")

        if min_rating is not None:
            params.append(f"minRating={min_rating}")

        if noodle is not None:
            params.append(f"noodle={noodle}")

        if me is not None:
            params.append(f"me={me}")

        if chroma is not None:
            params.append(f"chroma={chroma}")

        if cinema is not None:
            params.append(f"cinema={cinema}")

        if ranked is not None:
            params.append(f"ranked={ranked}")

        if full_spread is not None:
            params.append(f"full_spread={full_spread}")

        if auto_mapper is not None:
            params.append(f"automapper={auto_mapper}")

        if from_date is not None:
            params.append(f"from={from_date}")

        if to_date is not None:
            params.append(f"to={to_date}")

        params.append(f"sortOrder={sort_order.value}")

        if len(params) > 0:
            query += "?" + "&".join(params)

        search_response = await self._http_client.get(SearchResponse, query)
        return search_response.docs

    # /vote

    # TODO: Implement GET /vote

    # TODO: Implement POST /vote
