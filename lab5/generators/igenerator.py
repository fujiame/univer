from abc import ABC, abstractmethod
import numpy

class Igenerator(ABC):
    @abstractmethod
    def setParams(self, A: float, t: float, F: float) -> None:
        pass
    
    @abstractmethod
    def genSignal(self) -> numpy.ndarray:
        pass