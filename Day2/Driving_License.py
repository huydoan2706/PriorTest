from abc import ABC, abstractmethod


class Driving_License(ABC):
    @abstractmethod
    def vehicle_type(self):
        pass
