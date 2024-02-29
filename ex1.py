import re

def txt(text):
    a = "ab?"
    x = re.search(a, text)
    return x

print(txt("ab"))
print(txt("a0"))
print(txt("aaaaa"))
print(txt("abc"))
