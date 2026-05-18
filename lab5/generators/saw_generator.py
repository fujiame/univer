from generators import Igenerator
import numpy

class SawGenerator(Igenerator):
    __A: float = None
    __t: float = None
    __F: float = None
    __point: int = 1000
    __sinCount =  10000
    def __str__(self):
        return "Saw"
    
    def setParams(self, A: float, t: float, F: float):
        self.__A = A
        self.__t = t
        self.__F = F
        
    def genSignal(self):
        omega = 2 * numpy.pi * self.__F
        x = numpy.linspace(0, self.__t, self.__point)
        
        y = 0
        
        for n in range(1, self.__sinCount, 2):
            y += (-1)**((n-1)/2) * (numpy.sin(n * omega * x) / n**2)
        
        return x, y * (8 * self.__A/numpy.pi**2)