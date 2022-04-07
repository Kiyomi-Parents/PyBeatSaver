import asyncio
import logging
from asyncio import AbstractEventLoop
from datetime import datetime
from enum import Enum
from typing import Optional, TypeVar, Tuple, Dict, get_args, Type

import aiohttp
from aiohttp import ClientResponse, ClientResponseError

from .errors import BeatSaverAPIException, NotFoundException, ServerException
from .models.enum.base_enum import BaseEnum

T = TypeVar('T')


class HttpClient:
    MAX_TIMEOUT = 60

    def __init__(self, loop: Optional[AbstractEventLoop] = None):
        self.loop = loop
        self._aiohttp = None

    async def start(self):
        if self._aiohttp is None:
            self._aiohttp = aiohttp.ClientSession(loop=self.loop, raise_for_status=True)

    async def close(self):
        if self._aiohttp is not None:
            await self._aiohttp.close()
            self._aiohttp = None

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def _request(self, *args, params: Dict[str, str], **kwargs) -> ClientResponse:
        retries = 0

        while True:
            try:
                response = await self._aiohttp.request(*args, params=params, **kwargs)

                if response.status == 200:
                    return response

                raise BeatSaverAPIException(response.status, str(response.real_url),params)
            except ClientResponseError as error:
                status = error.status
                real_url = str(error.request_info.real_url)

                if status == 404:
                    raise NotFoundException(status, real_url, params) from error

            sleep = 10 * retries

            if sleep > self.MAX_TIMEOUT:
                sleep = 60

            logging.warning(f"Request failed! Waiting {sleep} seconds...")
            await asyncio.sleep(sleep)

            retries += 1

    def _format_params(self, params: Dict[str, any]) -> Dict[str, str]:
        for key, value in params.copy().items():
            if value is None:
                del params[key]
                continue

            params[key] = self._format_value(value)

        return params

    @staticmethod
    def _format_value(value: any) -> str:
        if isinstance(value, datetime):
            return str(1000 * int(value.timestamp()))

        if isinstance(value, bool):
            return "true" if value else "false"

        if isinstance(value, BaseEnum):
            return value.serialize

        if isinstance(value, Enum):
            return value.value

        if isinstance(value, list):
            items = []

            for item in value:
                items.append(HttpClient._format_value(item))

            return ",".join(items)

        return value

    async def get_raw(self, url, params: Dict[str, any] = None, *args, **kwargs):
        if params is None:
            params = {}

        response = await self._request('GET', url, params=params, *args, **kwargs)

        return await response.json()

    async def get(self, type_: Type[T], url: str, params: Dict[str, any] = None, *args: Tuple[any], **kwargs: Dict[str, any]) -> T:
        if params is None:
            params = {}

        params = self._format_params(params)

        response = await self._request('GET', url, params=params, *args, **kwargs)
        data = await response.json()

        if not get_args(type_):
            if isinstance(data, int):
                return data

            return type_.from_dict(data)

        return get_args(type_)[0].schema().load(data, many=True)
