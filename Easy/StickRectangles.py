seen = {}
num = 12
lengths = [1,2,3,4,1,2,3,4,8,4,7,5]
pair = 0

for num in lengths:
    if num in seen:
        seen[num] += 1
        if seen[num] % 2 == 0:
            pair += 1
    else: 
        seen[num] = 1

numRectangles = pair / 2
print(numRectangles)
    
