n = input("Enter the number of numbers you want to average out:")
sum = 0

for x in range(int(n)):
 num = input("Enter the number you want to average out:")
 sum = sum + float(num)
 
average = sum / float(n)
print("Average=",average)

