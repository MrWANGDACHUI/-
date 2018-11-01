n = int(input())
s = str(n)
#f = True

for i in range(len(s)//2):
    if s[i] !=  s[-1-i]:
        #f = False
        break

if f:
    print('%d是回文数字' % n)
else:
    print('%d不是回文数字' % n)
        
