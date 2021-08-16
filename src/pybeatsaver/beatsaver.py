import logging
from typing import Dict

from outcache import CacheAsync

from .httpClient import HttpClient
from .models.map_detail import MapDetail


class BeatSaver:
    TIMEOUT = 10
    _url = "https://api.beatsaver.com"

    def __init__(self):
        self.log = logging.getLogger(__name__)

        self._http = HttpClient()

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def start(self):
        await self._http.start()

    async def close(self):
        await self._http.close()

    async def _process_url(self, method: str, url: str) -> Dict:
        await self._http.start()

        return await self._http.request(method, url, timeout=self.TIMEOUT)

    @CacheAsync(hours=24)
    async def _get_map_by_hash(self, song_hash: str):
        return await self._process_url('GET', f"{self._url}/maps/hash/{song_hash}")

    async def get_map_by_hash(self, song_hash: str) -> MapDetail:
        map_info = await self._get_map_by_hash(song_hash)

        return MapDetail.from_dict(map_info)

    @CacheAsync(hours=24)
    async def _get_map_by_key(self, song_key: str):
        return await self._process_url('GET', f"{self._url}/maps/beatsaver/{song_key}")

    async def get_map_by_key(self, song_key: str) -> MapDetail:
        map_info = await self._get_map_by_key(song_key)

        return MapDetail.from_dict(map_info)
