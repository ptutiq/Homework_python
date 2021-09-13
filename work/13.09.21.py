def palindrom(n):
    
    b = n[::-1]
    if n == b:
        return ('True')
    else:
        return ('False')

print('введите строку ')
a = input()
print(palindrom(a))

def fail(string:str):
    return string.split('.')[1]

print('введите файл')
b = input()
print(fail(b))
    

def vremya(n):
    days = str(n  // 86400)
    n = n % 86400
    hours = str((n % 86400 ) // 3600)
    n = n % 3600
    minutes = str(n // 60)
    n = n % 60
    sek =str( n )
    return (days +':'+hours+':'+minutes+':'+sek)

print('введите время')
c = int(input())
print(vremya(c))

def Mnogo(n,k):
    b = n
    f = str(n)
    c = ''
    for i in range(k):
        g = f * k
        b += int(g)
    return(g)

print('введите число')
d = int(input())

print('введите количество повторов ')
k = int(input())
print(Mnogo(d,k))

