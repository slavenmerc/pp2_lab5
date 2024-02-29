import re
def txt(text):
    a = "ab{2,3}"
    if re.search(a, text):
            return "a matches b"
    else:
            return ("a doesn't match b")
print(txt("ab"))
print(txt("abbbbcc"))
print(txt("ddkkdkdkdkdk"))