import asyncio
import random
from unittest import IsolatedAsyncioTestCase

from src.pybeatsaver import BeatSaverAPI, NotFoundException


class TestBeatSaver(IsolatedAsyncioTestCase):
    _valid_map_hashes = [
        "4bbdaa1004a00eeb9c8d9432640e1c7d490b46d9",
        "000fbcb46c41cd0c363a80ae389333f7625e0921",
        "0078c298cbb2d6907a1d9c6ccc8b002935dd6f32",
        "00a1c30f22e0a7d9fd65e7ad64c5cb4b546e4503",
        "023c6a471ebdc243652cfaa26bcd71ba275bd770",
        "028f3a05eac78a51cb7ed51897fbd1dc5280b7d9"
    ]
    _invalid_map_hash = "4BDAA104A00E32EB9CD941132640E1C7490B4932"
    _valid_map_keys = [
        "19487",
        "fc05",
        "7d14",
        "1655b",
        "b820",
        "1dd"
    ]
    _invalid_map_key = "153423234235"
    _valid_user = 1344
    _valid_username = "schwnk"

    async def asyncSetUp(self) -> None:
        self.beatsaver = BeatSaverAPI(test_mode=True)

        await self.beatsaver.start()

    async def asyncTearDown(self) -> None:
        await self.beatsaver.close()

    async def test_beatmap_random(self):
        for index in range(5):
            await asyncio.sleep(0.2)
            random_key = hex(random.randint(1, int("1b501", 16)))[2:]

            try:
                map_detail = await self.beatsaver.beatmap(random_key)

                assert map_detail.versions[0].key == random_key
            except NotFoundException:
                pass

    async def test_beatmap_by_hash(self):
        beatmap = await self.beatsaver.beatmap_by_hash(self._valid_map_hashes[0])
        assert beatmap.versions[0].hash == self._valid_map_hashes[0]

    async def test_beatmaps_by_hashes(self):
        async for beatmap in self.beatsaver.beatmaps_by_hashes(self._valid_map_hashes):
            assert beatmap.versions[0].hash in self._valid_map_hashes

    async def test_user_beatmaps(self):
        beatmaps = await self.beatsaver.user_beatmaps(self._valid_user)

        for beatmap in beatmaps:
            assert beatmap.uploader.id == self._valid_user

    async def test_latest_beatmaps(self):
        beatmaps = await self.beatsaver.latest_beatmaps()

        for beatmap in beatmaps:
            assert beatmap.id is not None

    async def test_beatmaps_ordered_by_plays(self):
        beatmaps = await self.beatsaver.beatmaps_ordered_by_plays()

        for beatmap in beatmaps:
            assert beatmap.id is not None

    async def test_user(self):
        user = await self.beatsaver.user(self._valid_user)

        assert user.id == self._valid_user

    async def test_user_by_username(self):
        user = await self.beatsaver.user_by_username(self._valid_username)

        assert user.name == self._valid_username

    async def test_search_beatmaps(self):
        beatmaps = await self.beatsaver.search_beatmaps(search_question="ReeK - Weeaboo Spookfest [RANKED]")

        for beatmap in beatmaps:
            assert beatmap.id is not None

    async def test_beatmaps_by_keys(self):
        async for beatmap in self.beatsaver.beatmaps_by_keys(self._valid_map_keys):
            assert beatmap.id in self._valid_map_keys

    async def test_beatmaps_by_uploader(self):
        async for beatmaps in self.beatsaver.beatmaps_by_user(self._valid_user):
            for beatmap in beatmaps:
                assert beatmap.uploader.id == self._valid_user

    async def test_search_beatmaps_by_page(self):
        async for beatmaps in self.beatsaver.search_beatmaps_by_page(
            search_question="ReeK - Weeaboo Spookfest [RANKED]"
        ):
            for beatmap in beatmaps:
                assert beatmap.id is not None
