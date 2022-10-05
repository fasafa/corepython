import re
number=input('enter number')
rule='[a-z0-9._]+[@][a-z]+[.][comin]{2,3}'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")