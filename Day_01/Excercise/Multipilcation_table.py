try:

    number = int(input("Pick a number: "))
    for num in range(1, 10+1):
         answer = number * num
         print(f"{number}","x", f"{num}", "=",f"{answer}" )

except ValueError:
   print("Error! Please enter a number.")