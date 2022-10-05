import re
phn=input('enter number')
rule='[+][9][1]\d{10}'
matcher=re.fullmatch(rule,phn)
if matcher is not None:
    print("valid")
else:
    print("invalid")