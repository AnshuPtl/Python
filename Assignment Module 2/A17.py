#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap(s1,s2):
    f1=s1[:2]
    f2=s2[:2]

    swp1=f2+s1[2:]
    swp2=f1+s2[2:]

    ans=swp1+' '+swp2

    return ans

s1="ABCD"
s2="WXYZ"
s3="PQRS"
print(swap(s1,s2))
