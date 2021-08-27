class BeatSaverException(Exception):
    def __init__(self, status: int, url: str) -> None:
        self.status = status
        self.url = url

        super().__init__(f"Beat Saver returned {self.status} for {self.url}")


class NotFoundException(BeatSaverException):
    pass


class ServerException(BeatSaverException):
    pass
