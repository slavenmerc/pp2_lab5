import re
def txt(text):
        a = '^[A-Z]+[a-z]+$'
        if re.search(a,  text):
                return 'Upper case letters are followed by lower case letters'
        else:
                return('error')

print(txt("ABcbbbc"))
print(txt("aaAbAbbbc"))
print(txt("AAabbbc"))
print(txt("aababbbc"))
print(txt("AAAababbbc"))