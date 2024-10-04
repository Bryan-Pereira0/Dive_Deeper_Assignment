#task1 identify the greatest
#numb1 = int(input("Enter a number: "))
#numb2 = int(input("Enter a 2nd number: "))
#numb3 = int(input("Enter a 3rd number: "))
#if numb1>numb2 and numb1>numb3:
    #print(f"{numb1} is the greatest number.")
#elif numb3>numb2 and numb3>numb1:
    #print(f"{numb3} is the greatest number.")
#elif numb2>numb1 and numb2>numb3:
    #print(f"{numb2} is the greatest number.")
#task2 identify the smallest and greatest
numb1 = int(input("Enter a number: "))
numb2 = int(input("Enter a 2nd number: "))
numb3 = int(input("Enter a 3rd number: "))

if numb1>=numb2 and numb1>=numb3 and numb2>=numb3:
    print(f"{numb1} is the greatest number."), print(f"{numb3} is the smallest number.")
elif numb1<=numb2 and numb1<=numb3 and numb2>=numb3:
    print(f"{numb2} is the greatest number."), print(f"{numb1} is the smallest number.")
elif numb1>=numb2 and numb1<=numb3 and numb2<=numb3:
    print(f"{numb3} is the greatest number."), print(f"{numb2} is the smallest number.")
elif numb1<=numb2 and numb1<=numb3 and numb2<=numb3:
    print(f"{numb3} is the greatest number."), print(f"{numb1} is the smallest number.")
elif numb1>=numb2 and numb1>=numb3 and numb2<=numb3:
    print(f"{numb1} is the greatest number."), print(f"{numb2} is the smallest number.")
elif numb1<=numb2 and numb1>=numb3 and numb2>=numb3:
    print(f"{numb2} is the greatest number."), print(f"{numb3} is the smallest number.")
#there has to be an easier way to do this but I am brainfarting so hard so I am just going to bruteforce it lol.

