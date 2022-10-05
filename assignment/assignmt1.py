#explain the working of the given code
for i in range(2):      #i=0,1
    print(i)
    for j in range(5):      #j=0,1,2,3,4
        if j==3:            #0==3(not true),# 1==3(not true),2==3(not true),3==3(true)
            break           #break (stopped loop)
        else:
            print(j)        #0,1,2,

                            # output
                            # 0
                            # 0
                            # 1
                            # 2
                            # 1
                            # 1