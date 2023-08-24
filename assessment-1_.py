#22MIA1111 ANUSHA S
#ASSESMENT-1

import platform
import datetime
print(datetime.datetime.now())
print(platform.uname())
print("\n")

f1=open("/home/ex5/emails.txt","r")
f=f1.readlines()
f1.close()
res=[]
for i in range(len(f)):
         
         if "@" in f[i]:
                  if "." in f[i]:
                           if f[i] not in res:
                                res.append(f[i]) 
      
for i in range(0,len(res)-1):
         for j in range(i+1,len(res)):
                  if len(res[i])>len(res[j]):
                           res[i],res[j]=res[j],res[i]
print(res)

f2=open("/home/ex5/valid_emails.txt","w")
f2.writelines(res)
f2.close()

