user_leapyear= input("Enter the year:")
if int(user_leapyear) % 4 == 0:
    if int(user_leapyear) % 100 == 0:
        if int(user_leapyear) % 400 == 0:
            print(user_leapyear,"is leap year")
        else:
            print(user_leapyear,"is not a leap year")
else:
        print(user_leapyear,"is not a leap year")
        
    
                
        
    
        
        
    
