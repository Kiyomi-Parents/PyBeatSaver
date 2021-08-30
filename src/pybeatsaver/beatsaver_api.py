from typing import *

from .beatsaver import BeatSaver
from .errors import BeatSaverException
from .models import *
from .utils import split


class BeatSaverAPI(BeatSaver):

    async def beatmaps_by_keys(self, song_keys: List[str]) -> AsyncIterable[MapDetail]:
        for song_key in song_keys:
            yield await self.beatmap(song_key)

    async def beatmaps_by_hashes_all(self, beatmap_hashes: List[str]) -> AsyncIterable[List[MapDetail]]:
        chunks = split(beatmap_hashes, 50)
        for chunk in chunks:
            try:
                beatmaps = await self.beatmaps_by_hashes(chunk)

                if len(beatmaps) == 0:
                    break

                yield beatmaps

            except BeatSaverException:
                break

    async def beatmaps_by_user(self, user_id: int) -> AsyncIterable[List[MapDetail]]:
        """Returns async iterator so that you can async for loop over all the user maps by page"""
        page = 0
        while True:
            try:
                beatmaps = await self.user_beatmaps(user_id, page)

                if len(beatmaps) == 0:
                    break

                yield beatmaps

                page += 1

            except BeatSaverException:
                break

    async def search_beatmaps_by_page(self, *args, **kwargs) -> AsyncIterable[List[MapDetail]]:
        page = 0
        while True:
            try:
                beatmaps = await self.search_beatmaps(page=page, *args, **kwargs)

                if len(beatmaps) == 0:
                    break

                yield beatmaps

                page += 1

            except BeatSaverException:
                break
