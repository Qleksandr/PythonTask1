# letter A is number 65 in ASCI, so 1 = ord('A')-64

def nameProcessing(name):
    return(sum(ord(char)-64 for char in name))

dataFile = open('p022_names.txt', 'r')
dataString = (dataFile.readline()).replace('"', '')
dataFile.close()

dataList = sorted(dataString.split(','))

print(dataList)

elemList = [nameProcessing(elem) * (dataList.index(elem)+1) for elem in dataList]

print(elemList)

total = sum(elem for elem in elemList)

print(total)