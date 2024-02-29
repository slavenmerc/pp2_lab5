import re
def txt(text):
    a = "[a]*.?b$"
    if re.search(a, text):
            return "a matches b"
    else:
            return ("a doesn't match b")
print(txt("acb"))
print(txt("abbbbccb"))
print(txt("ddkkdkdkdkdk"))