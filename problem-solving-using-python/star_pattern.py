n=int(input("Enter the size of pattern"))
n+=1
for i in range(n):
    s=" "
    for j in range(i):
        s=s+"*"
    print(s)
