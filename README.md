[![PyPI version](https://badge.fury.io/py/PyBeatSaver.svg)](https://pypi.org/project/PyBeatSaver)
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
