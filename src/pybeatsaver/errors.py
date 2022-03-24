from typing import Dict


class PyBeatSaverException(Exception):
    pass


class BeatSaverAPIException(PyBeatSaverException):
    def __init__(self, status: int, url: str, params: Dict[str, str]) -> None:
        self.status = status
        self.url = url
        self.params = params

        super().__init__(f"Beat Saver returned {self.status} for {self.url}")


class NotFoundException(BeatSaverAPIException):
    pass


class ServerException(BeatSaverAPIException):
    pass
