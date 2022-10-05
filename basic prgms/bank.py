fixed_amount=(1000)
withdraw=int(input("enter amount to withdraw="))
if withdraw>=fixed_amount:
    print('insufficient balance')
else:
    print("your balace is ",fixed_amount)
# print('your balance is',fixed_amount-withdraw)
