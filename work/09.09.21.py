name = 'Yatsina Leonid Sergeevich'
def initals(name):
    lenght = len(name)
    names = []
    start = 0
    for i in range (len(name)):
        if name[i] == ' ':
            new_name = name[start:i]
            names.append(new_name)
            start = i + 1
        if i == len(name) - 1:
            names.append(name[start:i])
    return names[0] + ' ' + names[1][0:1] + '.' + names[2][0:1] + '.'
print(initals(name))


name.split()
names = name.split()
result =  names[0] + ' ' + names[1][0:1] + '.' + names[2][0:1] + '.'
print (result)