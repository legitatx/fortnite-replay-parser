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


class PlayerEliminationException(ReaderException):
    def __init__(self, detail: str = "Failed to parse elimination event."):
        super().__init__(detail)
