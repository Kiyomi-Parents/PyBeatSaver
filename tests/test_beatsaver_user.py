import pytest

from src.pybeatsaver import BeatSaver, BeatSaverAPI

valid_user = 1344
valid_username = "schwnk"


async def test_user_beatmaps(beatsaver: BeatSaver):
    beatmaps = await beatsaver.user_beatmaps(valid_user)

    for beatmap in beatmaps:
        assert beatmap.uploader.id == valid_user


async def test_user(beatsaver: BeatSaver):
    user = await beatsaver.user(valid_user)

    assert user.id == valid_user


async def test_user_by_username(beatsaver: BeatSaver):
    user = await beatsaver.user_by_username(valid_username)

    assert user.name == valid_username


async def test_beatmaps_by_uploader(beatsaver: BeatSaverAPI):
    if beatsaver.test_mode:
        return

    async for beatmaps in beatsaver.beatmaps_by_user(valid_user):
        for beatmap in beatmaps:
            assert beatmap.uploader.id == valid_user
