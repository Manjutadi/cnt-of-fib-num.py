#cnt of num when num is fibonacci
def isfib(num):
    if num==0 or num==1:
        return True
    a=0
    b=1
    cnt=3
    while True:
        c=a+b
        if c==num:
            return cnt
        if c>num:
            if c!=num:
                return False
        a=b
        b=c
        cnt+=1
