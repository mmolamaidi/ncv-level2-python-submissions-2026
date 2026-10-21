# Highest common factor problem
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if num1<num2:
    factor = num1
else:
    factor = num2
while num1%factor != 0 or num2%factor != 0:
    factor = factor - 1
    
print ("The highest common factor is: ", factor)