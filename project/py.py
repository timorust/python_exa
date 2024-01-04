string = "11221234"
resString = ""
length = len(string)

for i in range(length):
    for j in range(i, length):  
        subString = string[i:j + 1]
        # print(subString)
        if len(set(subString)) == len(subString) and len(subString) > len(resString):
            resString = subString 
print(resString)



