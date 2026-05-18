from generators import Igenerator
import numpy

class SinusGenerator(Igenerator):
    __A: float = None
    __t: float = None
    __F: float = None
    __point: int = 1000
    
    def __str__(self):
        return "Sinus"
    
    def setParams(self, A: float, t: float, F: float):
        self.__A = A
        self.__t = t
        self.__F = F
        
    def genSignal(self):
        omega = 2 * numpy.pi * self.__F
        x = numpy.linspace(0, self.__t, self.__point)
        y = self.__A * numpy.sin(omega * x)
        return x, y