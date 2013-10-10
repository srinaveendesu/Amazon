import sys
#input for first line
inp = raw_input()
l = len(inp)
dur = int(inp[2:l])
n= int(inp[0])
sh =[]
eh = []
sm = []
em = []
lst = []
time = {}
for i in range(0,1441):
    time[i] = 0


#taking input for other line
for i in range(n):
    lst.append(raw_input())
a=len(lst[0])

def check(i):
    if i==24:
        return 0
    return i

for i in range(n):
    if len(lst[i])>5:
        sh.append(int(lst[i][0:2]))
        sm.append(int(lst[i][3:5]))
        eh.append(int(lst[i][6:8]))
        em.append(int(lst[i][9:11]))
    else:
        sh.append(int(lst[i][0:2]))
        sm.append(int(lst[i][3:5]))
    st = sh[i]*60 + sm[i]
    et = eh[i]*60 + em[0]
    for j in range(st,et):
        time[j] = True
        
#print time
for i in range(1441):
    if (not time[i]):                
        for j in range(i,1441):
            if time[j]:
                break        
        if j-i >= dur:
            print j,i
            print check(i//60),check(i%60),check(j//60),check(j%60)
            
        i=j-1;   
        print i
        
    

