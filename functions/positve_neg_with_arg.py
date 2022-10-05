def pos_neg_check(n):
    if n>0:
        print('positive')
    elif n==0:
        print("zero")
    else:
        print('negative')
# pos_neg_check(-9)
# pos_neg_check(5)
# pos_neg_check(0)

number=int(input("enter number to check"))
pos_neg_check(number)