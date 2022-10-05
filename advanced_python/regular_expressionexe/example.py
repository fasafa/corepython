# import re
# count=0
# matcher=re.finditer('ab','abaaaaaabaaabaaabaab')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print(count)


# import re
# count=0
# x='[abc]'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)


# import re
# count=0
# x='[^abc]'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)
#
# import re
# count=0
# x='[a-z]'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)


# import re
# count=0
# x='[^A-Za-z0-9]'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)

# import re
# count=0
# x='\s'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)

# import re
# count=0
# x='\w'
# matcher=re.finditer(x,'avf cb@1234ABC')
# # print(matcher)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count=count+1
# print( "count =",count)