length=int(input('Enter the area length:'))
breath=int(input('Enter the peremeter breath: '))
area=length*breath
print('The area of the rectangle is:',area)
perimeter=2*(length+breath)
print('The paramiter is :',perimeter)
if area>perimeter:
    print('The area is greater than the paramiter')
else:
    print('the peremeter is greter then area')