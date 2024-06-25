sayi=int(input("Bir sayi degeri giriniz"))
for a in range(2,sayi+1):
    flag=0
    for b in range(2,a):
        if(a%b==0):
            flag=1
            break
    if(flag==0):
        print(a)
