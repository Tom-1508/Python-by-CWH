a = int(input("enter the number: "))
match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case 4:
        print("case is 4")
    case _:
        print("no match found")

# match case is added now from 3.10 version of python
        
# quick quiz : write a pyhton program to print table of a number which lies between 1 to 10
        
a = int(input("enter a number in between 1 to 10: "))
match a: 
    case 1: 
        for i in range(1,11,1):
            print("%d * %d = %d\n",a,i,a*i)
    case 2: 
        for i in range(1,11,1):
            print("%d * %d = %d\n",a,i,a*i)