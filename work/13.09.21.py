import time

#задание 1









#Задание 2







#Задание 3

def time(n):
    days = str(n  // 86400)
    n = n % 86400
    hours = str((n % 86400 ) // 3600)
    n = n % 3600
    minutes = str(n // 60)
    n = n % 60
    sek =str( n )
    return (days +':'+hours+':'+minutes+':'+sek)
print(days,':',hours,':',minutes,':',sek)





#Задание 4

#n = int(input()) 
#temp = str(n) 
#t1 = temp + temp 
#t2 = temp + temp + temp 
#comp = n + int(t1) + int(t2) 
#print(comp)