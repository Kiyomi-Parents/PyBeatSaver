import asyncio
import itertools

import pytest

from src.pybeatsaver import BeatSaverAPI


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(
    scope="session",
    params=itertools.product([True, False], [True, False])
)
async def beatsaver(event_loop, request):
    if request.param[0]:
        beatsaver_api = BeatSaverAPI(loop=event_loop, test_mode=request.param[1])
        await beatsaver_api.start()

        yield beatsaver_api

        await beatsaver_api.close()
    else:
        async with BeatSaverAPI(loop=event_loop, test_mode=request.param[1]) as beatsaver:
            yield beatsaver
