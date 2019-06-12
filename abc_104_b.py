from sys import stdin
import re

S = stdin.readline().rstrip()

pattern1 = r"^A([a-z])C([a-z]{1,7})$"
pattern2 = r'^A([a-z]){2}C([a-z]{1,6})$'
pattern3 = r'^A([a-z]){3}C([a-z]{1,5})$'
pattern4 = r'^A([a-z]){4}C([a-z]{1,4})$'
pattern5 = r'^A([a-z]){5}C([a-z]{1,3})$'
pattern6 = r'^A([a-z]){6}C([a-z]{1,2})$'
pattern7 = r'^A([a-z]){7}C([a-z]{1})$'

if (re.match("^A([a-z])C([a-z]{1,7})$", S)) or (re.match(pattern2, S)) or (re.match(pattern3, S)) or (re.match(pattern4, S)) \
        or (re.match(pattern5, S)) or (re.match(pattern6, S)) or (re.match(pattern7, S)):
    print('AC')
else:
    print('WA')
