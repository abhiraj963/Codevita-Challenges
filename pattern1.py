try:
    flag = 1
    while flag:
        N = int(input())
        if N > 1 or N < 101:
            flag = 0
except:
    print('enter a number')


gen1 = (x for x in range(1,(N*(N+1)) + 1))

def lst_first(m):
    lst_fst = []
    for i in range(0,m):
        lst_fst.append('*'*2*i)
    return lst_fst

def lst_middle(m):
    lst_mid = []
    for j in range(m,0,-1):
        lst_tmp = []
        for k in range(0,j):
            val = gen1.__next__()
            lst_tmp.append(str(val*10))
        lst_mid.append(''.join(lst_tmp))
    return lst_mid

def lst_last(m):
    lst_end = []
    for j in range(0,m):
        lst_tmp = []
        for k in range(0,j+1):
            val = gen1.__next__()
            lst_tmp.append(val*10)
        lst_tmp[-1] = int(lst_tmp[-1]/10)
        lst_tmp = [str(x) for x in lst_tmp]
        lst_end.append(''.join(lst_tmp))
    return lst_end[::-1]


for i,j,k in zip(lst_first(N),lst_middle(N),lst_last(N)):
    print(i+j+k)
    
                
