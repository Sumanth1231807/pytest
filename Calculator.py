def add2no(a,b):
    return a+b
def sub2no(a,b):
    return  a-b
def mul2no(a,b):
    return a*b
def div2no(a,b):
    return a/b

if __name__=="__main__":
    a=int (input("enter num1:"))
    b=int (input("enter num2:"))

    add=add2no(a,b)
    print(add)
    sub=sub2no(a,b)
    print(sub)
    mul=mul2no(a,b)
    print(mul)
    div=div2no(a,b)
    print(div)