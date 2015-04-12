f= open('d:/f1.txt','r')
# f.read()
var = int(f.read())
if var >200:
    ans= "Greater"
elif var <200:
    ans= "Smaller"
else:
    ans= "Equal"
print ans
f.close()
f= open('d:/f1.txt', 'r+')
f.write(ans)
f.close()

