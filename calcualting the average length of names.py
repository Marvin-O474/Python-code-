total_length = 0
colleagues_name = []
n = input("Insert number of names:")
for name in range(int(n)):
    name = input("Insert your collegues names:")
    total_length += len(name)
    colleagues_name.append(name)
average_length = total_length / len(colleagues_name)
print("Average length of names is",average_length)

    
