a=int(input('Enter the length:'))
b=int(input('Enter the length:'))
c=int(input('Enter the length:'))
if a==b==c:
    print('Equilateral Triangle')
elif a==b or b==c or c==a:
    print('Isosceles Triangle')
elif a != b and b!=c and  c!=a:
    print('Scalene Triangle')
elif a**2 + b**2 == c**2:
    print('Right Triangle')
else:
    print('Not a Triangle')
