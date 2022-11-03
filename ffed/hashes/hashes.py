from dataclasses import dataclass
from hashlib import new


@dataclass()
class LibraryHashes:
    algo: str

    def generate_hexdigest(self, input_string: str):
        return new(self.algo, input_string.encode()).hexdigest()
