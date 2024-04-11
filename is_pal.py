#Check whether string is Palendrome or not
def is_pal(str):
    len_str = len(str)
    c=0
    for i in range(len_str):
        if(str[i]==str[len_str-i-1]):
            continue
        else:
            c=1
            break
            print('Given String is Not Palendrome')

    return c == 0

print(is_pal('SSSS'))
