def duplicatechar(str):
    count = 0 
    strr  = str.split()
    for i in strr:
        for j in strr(i+1):
            if i == j:
                count+=1
            else: 
                continue
    print(i , count)

output = duplicatechar("NitiN")
print(output)


