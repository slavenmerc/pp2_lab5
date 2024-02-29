import re
def txt(text):
        a = '^[a-z]+_[a-z]+$'
        if re.search(a,  text):
                return 'lowercase letters are joined with underscopes'
        else:
                return('error')

s1 = txt("aab_cbbbc")
s1 += " some other string"
print(s1)
print(txt("aab_Abbbc"))
print(txt("aab_abbbc"))
print(txt("aababbbc"))
print(txt("AAAababbbc"))