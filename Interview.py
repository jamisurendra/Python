####CHECK IF SUM OF ANY TWO NUMBERS IS ZERO OR NOT

def add_num(l):
    if len(l) < 2:
        return False
    l1 = set(l)
    for i in l1:
        if -i in l1:
            return  True

    return False


l = [1,2]
print(add_num(l))

#### Adding 2 Numbers :

def add_numbers(x,y):
    x = x**2
    y = y**3
    return x + y

result= add_numbers(3,3)
print(result)

##  Print the values 
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

### Display 5 table 
count = 0

while count < 121:
    print(count)
    count += 5


