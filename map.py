a=[1,2,3,4,5,6]

def ad_6(a):
    return a+6

def fil_6(a):
    if(a>=7):
        return a

print("Mapped Input:",list(map(ad_6,a)))


print("Filtered Input:",list(filter(fil_6,a)))


