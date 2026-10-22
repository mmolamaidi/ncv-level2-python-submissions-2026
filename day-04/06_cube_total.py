import math

n = int(input("Enter a positive whole number (n): "))

if n < 1:
    print("Rejected")
else:
    total_cubes = 0
    for i in range(1, n + 1):
        # math.pow returns a float, so we convert it to int
        cube = int(math.pow(i, 3)) 
        print(cube, end=",")
        total_cubes += cube
        
    print(f"\nThe total of all cubes is: {total_cubes}")