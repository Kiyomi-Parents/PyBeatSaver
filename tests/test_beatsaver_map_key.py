import random

import pytest

from src.pybeatsaver import BeatSaver, NotFoundException, BeatSaverAPI

valid_map_keys = [
        "19487",
        "fc05",
        "7d14",
        "1655b",
        "b820",
        "1dd"
    ]


async def test_beatmap_random(beatsaver: BeatSaver):
    for index in range(5):
        random_key = hex(random.randint(1, int("1b501", 16)))[2:]

        try:
            map_detail = await beatsaver.beatmap(random_key)

            assert map_detail.id == random_key
        except NotFoundException:
            pass


@pytest.mark.parametrize("beatmap_key", valid_map_keys)
async def test_beatmap(beatsaver: BeatSaver, beatmap_key: str):
    map_detail = await beatsaver.beatmap(beatmap_key)

    assert map_detail.id == beatmap_key


async def test_beatmaps_by_keys(beatsaver: BeatSaverAPI):
    async for beatmap in beatsaver.beatmaps_by_keys(valid_map_keys):
        assert beatmap.id in valid_map_keys
