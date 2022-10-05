import re
number=input('enter number')
rule='^[a][\w\w]*[b]$'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")