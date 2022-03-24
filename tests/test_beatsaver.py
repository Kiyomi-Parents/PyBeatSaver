from src.pybeatsaver import BeatSaver, BeatSaverAPI


async def test_latest_beatmaps(beatsaver: BeatSaver):
    beatmaps = await beatsaver.latest_beatmaps()

    for beatmap in beatmaps:
        assert beatmap.id is not None


async def test_beatmaps_ordered_by_plays(beatsaver: BeatSaver):
    beatmaps = await beatsaver.beatmaps_ordered_by_plays()

    for beatmap in beatmaps:
        assert beatmap.id is not None


async def test_search_beatmaps(beatsaver: BeatSaver):
    beatmaps = await beatsaver.search_beatmaps(search_query="ReeK - Weeaboo Spookfest [RANKED]")

    for beatmap in beatmaps:
        assert beatmap.id is not None


async def test_search_beatmaps_by_page(beatsaver: BeatSaverAPI):
    async for beatmaps in beatsaver.search_beatmaps_by_page(
        search_query="ReeK - Weeaboo Spookfest [RANKED]"
    ):
        for beatmap in beatmaps:
            assert beatmap.id is not None
