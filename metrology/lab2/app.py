import numpy
import matplotlib.pylab as plt

filePath = r"data/2.txt"
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
print(data)

x = data[:, 0]
y = data[:, 1]

numBins = int(numpy.ceil(numpy.sqrt(len(y))))

plt.plot(x, y, "r o")
plt.xlabel("Pointsr")
plt.ylabel("Value")
plt.show()

plt.hist(y, bins=numBins, color="blue")
plt.show()

mean = numpy.mean(y)
sigma = numpy.std(y, ddof=1)
delta = numpy.sum(numpy.abs(y - mean)) / len(y)

s = sigma / numpy.sqrt(len(y))

t = 2.228
z = 1.96

if len(y) <= 20:
    dovInt = s * t
elif len(y) >= 20:
    dovInt = s * z
    
d = dovInt/mean * 100

print(f"Середнє значення: {mean}\nСтандартне кв.відхилення: {sigma}\nСередня похибка вимірювань: {delta}\nСтандартна похибка середнього: {s}\nАбсолютна похибка вимірювань: {dovInt}\nВідносна похибка вимірювань:{d} %")