def hello():
    print("Hello user!")
    
def pack(name,age,color):
    return [name,age,color]
    
def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is crazy ")
    else:
        for i in range(len(food)):
            if i==0:
                print (f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")
                
hello()
print(pack("natalia","20","orange"))
print(pack('natalia', 20, 'orange'))
eat_lunch([])
eat_lunch(["pasta"])
eat_lunch(["croissant","tacos","chips"])