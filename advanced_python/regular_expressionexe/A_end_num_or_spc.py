import re
number=input('enter number')
rule='[A-Z]*[0-9\W]'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")