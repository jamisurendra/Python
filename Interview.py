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
