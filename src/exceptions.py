class ReaderException(Exception):
    def __init__(
        self,
        detail: str = "An exception occurred.",
    ):
        self.detail = detail


class InvalidReplayException(ReaderException):
    def __init__(self, detail: str = "Failed to read replay file."):
        super().__init__(detail)


class ReadByteStringException(ReaderException):
    def __init__(self, detail: str = "End of string not zero."):
        super().__init__(detail)


class EventParseException(ReaderException):
    def __init__(self, detail: str = "Failed to parse replay event."):
        super().__init__(detail)


class PlayerEliminationException(EventParseException):
    def __init__(
        self, detail: str = "Failed to parse player elimination event."
    ):
        super().__init__(detail)
