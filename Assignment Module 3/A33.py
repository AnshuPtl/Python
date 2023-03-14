#Write a Python script to sort (ascending and descending) a dictionary by value.
d={5:8,20:1,65:24,90:11,36:97,540:215,982:346,456:702,124:132}

for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)

print("----------------------------------------------------------")

for k, v in sorted(d.items()):
    print(k, v)
