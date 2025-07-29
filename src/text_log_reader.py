from typing import Iterator

from .base_log_reader import BaseLogReader


class TextLogReader(BaseLogReader):
    """
    A simple log reader for plain text files. Each line is treated as
    a log entry.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    def open(self) -> None:
        self.file = open(self.filepath, "r", encoding="utf-8")

    def read(self) -> Iterator[str]:
        if self.file is None:
            raise RuntimeError("Log file not opened. Call open() first.")
        for line in self.file:
            yield line.rstrip("\n")

    def close(self) -> None:
        if self.file is not None:
            self.file.close()
            self.file = None
