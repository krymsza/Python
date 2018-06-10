def r(n):
    slo={}
    for i in range(int(2) , int(n-1)):
        while(n>0 and n%i ==0):
            if(n%i==0):
                if(i in slo):
                    slo[i] = slo[i]+1
                else:
                    slo[i] = 1
                n = n/ i
    list = []
    for i in slo.keys():
        list.append((i, slo[i]))
    print(list)
    
r(756)
