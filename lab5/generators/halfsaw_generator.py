from generators import Igenerator
import numpy

class HalfSawGenerator(Igenerator):
    __A: float = None
    __t: float = None
    __F: float = None
    __point: int = 1000
    __sinCount =  10000
    def __str__(self):
        return "HalfSaw"
    
    def setParams(self, A: float, t: float, F: float):
        self.__A = A
        self.__t = t
        self.__F = F
        
    def genSignal(self):
        omega = 2 * numpy.pi * self.__F
        x = numpy.linspace(0, self.__t, self.__point)
        
        y = 0
        
        for n in range(1, self.__sinCount):
            y += numpy.sin(n * omega * x) / n
        
        return x, (self.__A/2 - y * self.__A/numpy.pi)