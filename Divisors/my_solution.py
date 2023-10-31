num = int(input("Enter a number: \n"))

numberList = []

rangeList = list(range(1,num+1))

for i in rangeList:
    if num % i == 0:
        numberList.append(i)
        
print(numberList)