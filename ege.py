r=int(input('Enter the ege:'))
s=int(input('Enter the ege:'))
a=int(input('Enter the ege:'))

if r>s and r>a:
    youngest='r'
elif s>r and s>a:
    youngest='s'
elif a>r and a>s:
    youngest='a'
print(f"The youngest is: {youngest}")