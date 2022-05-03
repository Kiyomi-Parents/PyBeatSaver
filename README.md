[![GitHub license](https://img.shields.io/github/license/Kiyomi-Parents/PyBeatSaver)](https://github.com/Kiyomi-Parents/PyBeatSaver/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/PyBeatSaver.svg)](https://pypi.org/project/PyBeatSaver)
[![codecov](https://codecov.io/gh/Kiyomi-Parents/PyBeatSaver/branch/master/graph/badge.svg?token=IUFZTBDVEE)](https://codecov.io/gh/Kiyomi-Parents/PyBeatSaver)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/pybeatsaver.svg)](https://pypi.org/project/PyBeatSaver)
[![PyPI downloads](https://img.shields.io/pypi/dm/pybeatsaver?color=blueviolet&logo=pypi)](https://pypi.org/project/PyBeatSaver)
# PyBeatSaver
Beat Saver API client

Comes with caching and rate limiting out of the box.

There is also a test mode which can be enabled like this ```beatsaver = BeatSaverAPI(test_mode=True)```.
This will return random data instead of making API requests to Beat Saver.

### Usage:
```python
import asyncio
from pybeatsaver import BeatSaverAPI


async def main():
    async with BeatSaverAPI() as beatsaver:
        beatmap = await beatsaver.beatmap("16d22")
        print(beatmap)

# Get fake data instead
async def main_fake():
    async with BeatSaverAPI(test_mode=True) as beatsaver:
        beatmap = await beatsaver.beatmap("16d22")
        print(beatmap)

asyncio.run(main())
asyncio.run(main_fake())
```

### Faker provider:
```python
from faker import Faker
from pybeatsaver import BeatSaverProvider

faker = Faker()
faker.add_provider(BeatSaverProvider)

beatmap = faker.map_detail()
print(beatmap)
```
