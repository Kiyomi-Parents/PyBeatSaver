import asyncio

import pytest

from src.pybeatsaver import BeatSaverAPI


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", params=[False, True])
async def beatsaver(event_loop, request):
    beatsaver_api = BeatSaverAPI(loop=event_loop, test_mode=request.param)
    await beatsaver_api.start()

    yield beatsaver_api

    await beatsaver_api.close()
