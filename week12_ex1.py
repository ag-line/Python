import re
str = "Oh My love is red red Rose 123 156 11 3456 A AA AAA ab abab ababab abc"
def chkRexp(ptn,str):
    str = str.split()
    for w in str:
        found = re.search(ptn,w)
        if found:
            if found.group() != "":
              print(found.group(),end=" ")

chkRexp("[ab]+",str) #ab abab ababab ab
print("")
chkRexp("A*",str) #A AA AAA
print("")
chkRexp("[0-9]*",str) #123 156 11 3456
print("")
chkRexp("^[1-9]{4}",str) #3456
print("")
chkRexp("^[A-Z]",str)#O M R A A A
print("")
chkRexp("[a-z]$",str) #h y e s d d e b b b c 