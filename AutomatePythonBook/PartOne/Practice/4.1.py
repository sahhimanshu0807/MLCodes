# Create a list of 5 numbers
# Print the list, max, min, length, and sum

listNum = [x for x in range(10,20) if x % 2 == 0]
print(listNum)
print(min(listNum))
print(max(listNum))
print(len(listNum))

sumNum = 0
for x in listNum:
    sumNum += x

print(sumNum)
print(sum(listNum))