
num = int(input("Enter a five-digit number: "))
if 10000 <= num <= 99999:
    original_num = num  
    reverse_num = 0
    
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10

    if original_num == reverse_num:
        print("The number {original_num} is valid.")
    else:
        print("The number {original_num} is not a valid.")
else:
    print("Please enter a valid five-digit number.")
