# /app/ordo_missa/ordo_missa_abc.py

from abc import ABC, abstractmethod


class OrdoMissaABC(ABC):
    def __init__(self, num_deacons: int, num_servers: int):

        # Validate the class initalization:
        if num_deacons not in [0, 1, 2]:
            raise ValueError("Number of deacons must be 0, 1, or 2.")
        if num_servers < 0:
            raise ValueError("Number of servers must be 0 or greater.")

        self.num_deacons = num_deacons
        self.num_servers = num_servers

    @abstractmethod
    def introductory_rites(self) -> str:
        """Generate the Introductory Rites of the Mass."""
        pass

    @abstractmethod
    def liturgy_of_the_word(self) -> str:
        """Generate the Liturgy of the Word."""
        pass

    @abstractmethod
    def liturgy_of_the_eucharist(self) -> str:
        """Generate the Liturgy of the Eucharist."""
        pass

    @abstractmethod
    def communion_rite(self) -> str:
        """Generate the Communion Rite."""
        pass

    @abstractmethod
    def concluding_rites(self) -> str:
        """Generate the Concluding Rites of the Mass."""
        pass
