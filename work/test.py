import string
import itertools

def alphanumeric_strings():
    for n in itertools.count():
        for t in itertools.product(string.ascii_letters + string.digits, repeat=n):
            yield ''.join(t)

