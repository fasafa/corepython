import re
number=input('enter number')
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
matcher=re.fullmatch(rule,number)
if matcher is not None:
    print("valid")
else:
    print("invalid")