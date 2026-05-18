import numpy
import matplotlib.pylab as plt

filePath = r"data/2_1.txt"
filePath2 = r"data/2_2.txt"
data = []

with open(filePath, "r") as file:
    file.readline()
    for line in file:
        row = line.strip().split()
        if not row: continue 
        
        row[0] = int(row[0])
        row[1] = float(row[1].replace(",", "."))
        data.append(row)


data = numpy.array(data)

data2 = []

with open(filePath2, "r") as file:
    file.readline()
    for line in file:
        row = line.strip().split()
        if not row: continue 
        
        row[0] = int(row[0])
        row[1] = float(row[1].replace(",", "."))
        data2.append(row)


data2 = numpy.array(data2)


x = data[:, 0]
y = data[:, 1]

y2 = data2[:, 1]

numBins = int(numpy.ceil(numpy.sqrt(len(y))))
numBins2 = int(numpy.ceil(numpy.sqrt(len(y2))))


plt.plot(x, y, "r o")
plt.plot(x, y2, "b o")
plt.xlabel("Number")
plt.ylabel("Value")
plt.show()

plt.hist(y, bins=numBins, color="red")
plt.show()
plt.hist(y2, bins=numBins, color="blue")
plt.show()

mean1 = y.mean()
mean2 = y2.mean()
sigma1 = y.std(ddof=1)
sigma2 = y2.std(ddof=1)

difmean = mean2 - mean1

sigma5 = 5 * sigma1

print("======= Дані =======")
print(data)
print(data2)
print(numpy.ceil(numpy.sqrt(len(y))))
print()
print(f"Середнє значення для величини №1: {mean1}")
print(f"Середнє значення для Величини №2: {mean2}")
print(f"Стандартне відхилення для величини №1 (sigma1): {sigma1}")
print(f"Стандартне відхилення для величини №2 (sigma2): {sigma2}")
print(f"Різниця середніх значень величин №1 і №2: {difmean}")
print(f"Значення 5 * sigma: {sigma5}")