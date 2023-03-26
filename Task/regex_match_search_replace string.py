# match string, search in string, replace string

import re #will import the module RegEx

string = "Hello All"

pattern1 = "He"

pattern2 = "lo"

pattern = "World"

#will match the beginning of string
print(re.match(pattern1,string))

print(re.search(pattern2,string))

print(re.sub("All",pattern,string))
