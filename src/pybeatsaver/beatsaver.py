import logging
from json.decoder import JSONDecodeError
from typing import Dict

import requests
from outcache import Cache

from .common import Common
from .models.map_detail import MapDetail


class BeatSaver:
    TIMEOUT = 10
    _url = "https://api.beatsaver.com"

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def _process_url(self, url: str) -> Dict:
        response = Common.request(requests.get, url, timeout=self.TIMEOUT)

        try:
            data = response.json()
        except JSONDecodeError:
            self.log.exception("JSONDecodeError, response: %r, response.text: %r", response, response.text)
            data = {"error": "Failed to decode json from BeatSaver. Somethings broken."}

        return data

    @Cache(hours=24)
    def _get_map_by_hash(self, song_hash: str):
        return self._process_url(f"{self._url}/maps/hash/{song_hash}")

    def get_map_by_hash(self, song_hash: str) -> MapDetail:
        map_info = self._get_map_by_hash(song_hash)

        return MapDetail.from_dict(map_info)

    @Cache(hours=24)
    def _get_map_by_key(self, song_key: str):
        return self._process_url(f"{self._url}/maps/beatsaver/{song_key}")

    def get_map_by_key(self, song_key: str) -> MapDetail:
        map_info = self._get_map_by_key(song_key)

        return MapDetail.from_dict(map_info)
