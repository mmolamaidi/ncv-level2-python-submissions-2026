marks = []

i=0

mark = int(input("Enter mark (or -1 to stop): "))
while mark !=-1:
    marks.append(mark)
    i += 1
    mark = int(input("Enter mark (or -1 to stop): "))
    
print("         ")   
print(f'our list has  {len(marks)} elements')

total = 0

for x in range(len(marks)):
    mark = marks[x]
    total += mark
    print(marks[x])
    
sum = total
avg = total/len(marks)

print("         ")
print(f'The sum of all marks = {sum}')
print("         ")
print(f'The average of all marks = {avg:.2f}')