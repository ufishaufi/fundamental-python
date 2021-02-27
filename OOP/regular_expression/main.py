import re

pattern = r"eggs"

# if re.match(pattern, "eggseggseggs"):
# if re.match(pattern, "baconeggseggseggsbacon"):
if re.match(pattern, "eggseggseggsbacon"):
    print('Match found')
else:
    print('No match found')

# search and findAll
if re.search(pattern, "baconeggseggseggsbacon"):
    print('Match found')
else:
    print('No match found')

print(re.findall(pattern, "baconeggseggsbacon"))

# find and replace

string = "My name is John, Hi I'm john"
pattern = r"John"
newstring = re.sub(pattern, "Rob", string)
print(newstring)

# The dot metacharacter
pattern = r"gr.y"

if re.match(pattern, "gray"):
    print('Match found')

# caret & dollar metacharacter
# caret => ^ di awal
# dollar => $ di akhir
pattern = r"^gr.y$"

if re.match(pattern, "grby"):
    print('Match 1')

# character class
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AA6"):
    print('Match found')

# star metacharacter
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggs"):
    print('Match found')

# group
pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadbread"):
    print('Match found')