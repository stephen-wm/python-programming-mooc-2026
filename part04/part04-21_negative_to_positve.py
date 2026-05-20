number = int(input("Please type in a positive integer: "))
 
for num in range(-number, number + 1):
    if num == 0:
        continue;
    
    print(num)
 