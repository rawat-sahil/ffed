from abc import ABC, abstractmethod


class AbstractEncoderDecoder(ABC):
    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def decode(self):
        pass
