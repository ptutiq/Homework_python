import string
def count_letters(text):
    a = {}
    for ch in string.ascii_letters:
        d[ch] = text.count(ch)
    return d
def count_letters(text):
    return{ch:text.count(ch) for ch in string.ascii_letters}