import abc
from typing import Any, Iterator


class BaseLogReader(abc.ABC):
    """
    Abstract base class for log readers. Each reader must handle open,
    read, close, and optional seek operations.
    """

    @abc.abstractmethod
    def open(self) -> None:
        """
        Open the log source (file, stream, etc.).
        """
        ...

    @abc.abstractmethod
    def read(self) -> Iterator[Any]:
        """
        Yield raw log records.

        Returns:
            An iterator over parsed log entries.
        """
        ...

    @abc.abstractmethod
    def close(self) -> None:
        """
        Close the log source and release resources.
        """
        ...

    def seek(self, position: Any) -> None:
        """
        Reposition to a given point in the log.

        Readers can override if they support seeking; otherwise this
        raises NotImplementedError.
        """
        raise NotImplementedError("Seek not implemented for this reader")
