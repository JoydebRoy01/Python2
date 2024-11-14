book_return=int(input('Enter the days of book_return:'))
if book_return<=5:
    print("Fine is 0.5 Paisa")
elif book_return<=10:
    print("Fine is 5 Paisa")
elif book_return <=30:
    fine=(5*0.50)+(5*1)+((book_return-10)*5)
    print (f'The fine is {fine} rupees')
else:

    print('Member ship is cancel')
