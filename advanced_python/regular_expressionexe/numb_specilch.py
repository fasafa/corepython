import re
number=input('enter number')
rule='[\d]{2}\W+'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")