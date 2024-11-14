x1 = int(input('Enter the number: '))
y1 = int(input('Enter the number: '))
x2 = int(input('Enter the number: '))
y2 = int(input('Enter the number: '))
x3 = int(input('Enter the number: '))
y3 = int(input('Enter the number: '))

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print('Both sides are equal.')
else:
    print('Both sides are not equal.')
