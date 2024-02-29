import re

def snakecamel(snake):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake)

# Example usage
snaketxt = input()
cameltxt = snakecamel(snaketxt)

print(cameltxt)
