n=int((input("Please insert a value:  ")))

for i in range(0,n):
    list = []

    command=(input("Please enter the command:"))
    if command=="insert":
        list.insert(2,10)
        print (list)
        break

    elif command=="remove":
        list.remove(10)
        print (list)
        break


    elif command=="append":
        list.append(10)
        print (list)
        break   

    elif command=="sort":
        list.sort()
        print (list)
        break

    elif command=="pop":
        list.pop()
        print (list)
        break

    elif command=="reverse":
        list.reverse()
        print (list)
        break
        
    else:
        print("Enter a Valid command")
        print (list)
