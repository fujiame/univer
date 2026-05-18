import numpy
import matplotlib.pylab as plt

filePathMeasures = r"data/measures_1.txt"
filePathEtalon = r"data/measures_2_etalon.txt"
dataMeasures = []
dataEtalon = []

with open(filePathMeasures, "r") as file:
    file.readline()
    for line in file:
        row = line.strip().split()
        if not row: continue 
        
        row[0] = int(row[0])
        row[1] = float(row[1].replace(",", "."))
        dataMeasures.append(row)
        
with open(filePathEtalon, "r") as file:
    file.readline()
    for line in file:
        row = line.strip().split()
        if not row: continue 
        
        row[0] = int(row[0])
        row[1] = float(row[1].replace(",", "."))
        dataEtalon.append(row)


dataMeasures = numpy.array(dataMeasures, dtype=float)[:, 1:]
dataEtalon = numpy.array(dataEtalon, dtype=float)[:, 1:]

nMeasurements = 10
t = 2.228

meanMeasures = numpy.mean(dataMeasures, axis=0) #середнє значення
sigmaMeasures = numpy.std(dataMeasures, ddof=1, axis=0) #середнє кв.відхилення
sMeasures = sigmaMeasures / numpy.sqrt(nMeasurements) #середня статистична похибка
deltaMeasures = sigmaMeasures * t #довірчий інтервал (абсолютна похибка)
deltaAVGMeasures = numpy.mean(deltaMeasures)


meanEtalon = numpy.mean(dataEtalon, axis=0) #середнє значення
sigmaEtalon = numpy.std(dataEtalon, ddof=1, axis=0) #середнє кв.відхилення
sEtalon = sigmaEtalon / numpy.sqrt(nMeasurements) #середня статистична похибка
deltaEtalon = sEtalon * t #довірчий інтервал (абсолютна похибка)
deltaAVGEtalon = numpy.mean(deltaEtalon)

deltaS = meanMeasures - meanEtalon
deltaSAVG = numpy.mean(deltaS)

print("==================== Мультиметр ====================")
print(f"Середні значення: {meanMeasures}")
print(f"Середнє кв. відхилення: {sigmaMeasures}")
print(f"Середня стат. похибка: {sMeasures}")
print(f"Довірчий інтервал: {deltaMeasures}")
print(f"Усереднена випадкова похибка: {deltaAVGMeasures}")
print()
print("==================== Еталон ====================")
print(f"Середні значення: {meanEtalon}")
print(f"Середнє кв. відхилення: {sigmaEtalon}")
print(f"Середня стат. похибка: {sEtalon}")
print(f"Довірчий інтервал: {deltaEtalon}")
print(f"Усереднена випадкова похибка: {deltaAVGEtalon}")
print()
print(f"Систематичні похибки: {deltaS}")
print(f"Усереднене значення систематичної похибки: {deltaSAVG}")
