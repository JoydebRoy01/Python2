a=float(input('Enter the sides:'))
b=float(input('Enter the sides:'))
c=float(input('Enter the sides:'))
largest=max(a,b,c)
if a+b>c and a+c>b and b+c>a:
    print('Valid Triangle')
else:
    print('not valid')