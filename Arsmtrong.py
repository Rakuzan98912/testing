 n=int(input("Enter the number:"))
 t=n
 r=0
 while(n>0):
 a=n%10
 r=r+a*a*a
 n=n//10
 if(r==t):
     print("Armstrong number")
     else:
         print("Not an Armstrong number")
