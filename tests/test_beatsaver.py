from unittest import IsolatedAsyncioTestCase

from src.pybeatsaver import NotFoundException
from src.pybeatsaver.beatsaver import BeatSaver


class TestBeatSaver(IsolatedAsyncioTestCase):
    _valid_map_hash = "4bbdaa1004a00eeb9c8d9432640e1c7d490b46d9"
    _invalid_map_hash = "4BDAA104A00E32EB9CD941132640E1C7490B4932"
    _valid_map_key = "19487"
    _invalid_map_key = "153423234235"

    def setUp(self):
        self.beatsaver = BeatSaver()

    async def test_get_map_by_hash_valid(self):
        async with self.beatsaver as beatsaver:
            map_detail = await beatsaver.get_map_by_hash(self._valid_map_hash)
            self.assertEqual(map_detail.versions[0].hash, self._valid_map_hash)

    async def test_get_map_by_hash_invalid(self):
        async with self.beatsaver as beatsaver:
            with self.assertRaises(NotFoundException):
                await beatsaver.get_map_by_hash(self._invalid_map_hash)

    async def test_get_map_by_key(self):
        async with self.beatsaver as beatsaver:
            map_detail = await beatsaver.get_map_by_key(self._valid_map_key)

            self.assertEqual(map_detail.versions[0].key, self._valid_map_key)

    async def test_get_map_by_key_invalid(self):
        async with self.beatsaver as beatsaver:
            with self.assertRaises(NotFoundException):
                await beatsaver.get_map_by_key(self._invalid_map_key)
