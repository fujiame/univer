from generators import Igenerator
import numpy

class MeanderGenerator(Igenerator):
    __A: float = None
    __t: float = None
    __F: float = None
    __point: int = 1000
    __sinCount =  10000
    def __str__(self):
        return "Meander"
    
    def setParams(self, A: float, t: float, F: float):
        self.__A = A
        self.__t = t
        self.__F = F
        
    def genSignal(self):
        omega = 2 * numpy.pi * self.__F
        x = numpy.linspace(0, self.__t, self.__point)
        
        y = 0
        
        for n in range(1, self.__sinCount, 2):
            y += numpy.sin(n * omega * x) / n
        
        return x, y * (4 * self.__A / numpy.pi)