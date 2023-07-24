name = input("Insert your name:")
letters =('a','b','c','d','e','f','g','h','i','j','k','l','n')
second_half = name.lower().startswith(letters)

if second_half:
    print(name,"is in first half of the alphabet")
else:
    print(name,"is in second half of the alphabet")

