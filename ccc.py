def f(n):
    last=1
    secondlast=1
    i=2
    while i<n:
        current=last+secondlast
        secondlast=last
        last=current
        i+=1
    return current
print(f(10))
