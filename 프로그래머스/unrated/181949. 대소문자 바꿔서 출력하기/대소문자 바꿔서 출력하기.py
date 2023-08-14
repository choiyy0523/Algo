str = input()

for s in str:
    if s.islower():
        s = s.upper()
    else:
        s = s.lower()
    print(s, end='')
