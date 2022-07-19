from pprint import pprint

import pytest

from src.pybeatsaver import BeatSaver, BeatSaverAPI, PyBeatSaverException

valid_map_hashes = [
    "4bbdaa1004a00eeb9c8d9432640e1c7d490b46d9",
    "000fbcb46c41cd0c363a80ae389333f7625e0921",
    "0078c298cbb2d6907a1d9c6ccc8b002935dd6f32",
    "00a1c30f22e0a7d9fd65e7ad64c5cb4b546e4503",
    "023c6a471ebdc243652cfaa26bcd71ba275bd770",
    "028f3a05eac78a51cb7ed51897fbd1dc5280b7d9"
]

updated_map_hashes = [
    'de7b5e933dd79d06ddee3df71174019cbe9ebd45',  # Returns map with hash b3574125c2c8d6e187d4b7c5d59b5bb625fd2217
    'e5048cca03e1a41c25915246a02106095011f91d'  # Returns map with hash b3a1950f5974db1ccab5c09c500ab3cbb77980c0
]


@pytest.mark.parametrize("beatmap_hash", valid_map_hashes)
async def test_beatmap_by_hash(beatsaver: BeatSaver, beatmap_hash: str):
    beatmap = await beatsaver.beatmap_by_hash(beatmap_hash)
    assert beatmap.versions[0].hash == beatmap_hash


@pytest.mark.parametrize("beatmap_hash", updated_map_hashes)
async def test_beatmap_by_hash_wrong(beatsaver: BeatSaver, beatmap_hash: str):
    if not beatsaver.test_mode:
        beatmap = await beatsaver.beatmap_by_hash(beatmap_hash)
        assert beatmap.versions[0].hash != beatmap_hash


async def test_beatmaps_by_hashes(beatsaver: BeatSaver):
    for beatmap in await beatsaver.beatmaps_by_hashes(valid_map_hashes):
        assert beatmap.versions[0].hash in valid_map_hashes


async def test_beatmaps_by_hashes_overflow(beatsaver: BeatSaver):
    with pytest.raises(PyBeatSaverException):
        for beatmap in await beatsaver.beatmaps_by_hashes(valid_map_hashes * 10):
            assert beatmap is not None


async def test_beatmaps_by_hashes_all(beatsaver: BeatSaverAPI):
    async for beatmaps in beatsaver.beatmaps_by_hashes_all(valid_map_hashes):
        assert len(beatmaps) == len(valid_map_hashes)


async def test_beatmaps_by_hashes_all_single(beatsaver: BeatSaverAPI):
    async for beatmaps in beatsaver.beatmaps_by_hashes_all([valid_map_hashes[0]]):
        assert beatmaps[0].versions[0].hash == valid_map_hashes[0]

