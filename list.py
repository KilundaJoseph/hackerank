n=int((input("Please insert a value:  ")))

# for i in range(0,n):
list = []
for i in range(n):
    list.append(i)
print(list,end=" ")


x= int(input("number"))
command=(input("Please enter the command:"))
if command=="insert":
    list.insert(2,x)
    print (list)
        # break
    for i in list:
        # i=x
        command=(input("Please enter the command:"))

        if command=="remove":
            list.remove(x)
            print (list)
            # break


        elif command=="append":
            list.append(x)
            print (list)
            # break   

        elif command=="sort":
            list.sort()
            print (list)
            # break

        elif command=="pop":
            list.pop()
            print (list)
            # break

        elif command=="reverse":
            list.reverse()
            print (list)
            # break
            
    else:
        print("Enter a Valid command")
        print (list)






        # list=(5,124,75,61,47,85,10,1,6,2,4,)

# even, odd = count(list)
# print (even)
# print(odd)

