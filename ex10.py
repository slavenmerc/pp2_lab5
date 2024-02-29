from re import sub
def snake(txt):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        txt.replace('-', ' '))).split()).lower()
print(snake('aaAAAaa'))
print(snake('HelloWorld'))
