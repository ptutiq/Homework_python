import string
alfavit1 =[]
alfavit1.append(string.ascii_lowercase)
print(alfavit1)


alfavit = []
for i in range(97,123):
    alfavit.append(chr(i))
print(alfavit)

string = (string.ascii_lowercase)
alfavit2 = []
for i in range (26):
    alfavit2.append(string[i])
print(alfavit2)


def get_elements_for(list_):
    k = 0
    while k < len(list_):
        print(list_[k])
        k += 1
        
def show(func):
    def new_func(*args, **kwargs):
        print ('Name of function -', func._name_)
        print('agrs -', args)
        print('kwargs -', kwargs)
    return new_func

