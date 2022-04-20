#s  = '7' * 2022
#while '777' in s or '333' in s:
#    s = s.replace('777','3',1)
#    s = s.replace('333','7',1)
#print(s)



#print('x y z w')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if((x <= y) and ((not x) <= (not z)) or w) == 0:
#                   print(x,y,z,w)


#for n in range(1,1000):
#    b = bin(n)[2:]
#    if n % 2 == 0:
#        b += '10'
#    else:
#        b +='11'
#    if(b.count('1') % 2 ==0):
#       b +='0'
#    else:
#        b +='1'
#    r = int(b,2)
#    if r > 53:
#        print(n)
    
#for i in range(1,1000):
#    s = i
#    n = 200
#    while s > 0:
#        s = s // 4
#        n = n - 6
#    if (n == 170):
#        print(i)


#print(120/2/2*3)


#s = 16 ** 23 + 4 ** 12 - 32 ** 6
#c0 = 0
#c1 = 0
#c2 = 0
#c3 = 0
#while s > 0 :
#    if (s % 4 == 0):
#        c0 += 1
#    elif(s % 4 == 1):
#        c1 += 1
#    elif(s % 4 == 2):
#        c2 += 1
#    elif(s % 4 == 3):
#        c3 += 1
#    s = s // 4
#print(c0, c1, c2, c3)


#s=[0]*300
#s[2] = 1
#for i in range(2, 13):
#    s[i+1] += s[i]
#    s[i*3] += s[i]
#x = s[12]
#s=[0] * 300
#s[12] = x
#for i in range(12, 72):
#    s[24] = 0
#    s[i+1] += s[i]
#    s[i*3] += s[i]
#print(s[72])


#for i in range(1,1000):
#    x = i
#    L = 0
#    M = 0
#    while x > 0:
#        L = L+1
#        if M < (x % 8):
#            M = x % 8
#        x = x // 8
#        if (L == 4 and M == 7):
#            print(i)


#for a in range(1, 10000):
#  flag = 1
#  for x in range(1, 10000):
#    if ((x % 54 != 0 or x % 80 != 0) <= (x % a != 0)) == 0:
#      flag = 0
#      break
#  if flag == 1:
#    print(a)


a = []
for i in range(5000):
    a.append(int(input()))
ans = []
for i in range(len(a) - 1):
  if a[i] % 4 == 0 and a[i + 1] % 4 == 0:
    ans.append(a[i] + a[i + 1])
print(len(ans), max(ans))          
