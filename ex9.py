import re
def capital_words_spaces(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)
print(capital_words_spaces("AAaaaAAA"))
print(capital_words_spaces("HelloWorld"))
