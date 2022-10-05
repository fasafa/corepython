import re
number=input('enter number')
rule='\w{3,8}'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")