largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try: 
        num = float(inp)
    except:
        print("Invalid input")
        continue
        
    if smallest is None:
        smallest = num
        largest = num
    if num < smallest:
        smallest = num 
    elif num > largest:
        largest = num 
        
print("Maximum is", int(largest))
print("Minimum is", int(smallest))

 

