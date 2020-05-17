S = 'あいうんー'


def successive_bar(s):
    if s[1] == s[2] == 'ー' or s[2] == s[3] == 'ー' or s[3] == s[4] == 'ー':
        return True
    else:
        return False

for a in S:
    for b in S:
        for c in S:
            for d in S:
                for e in S:
                    if a not in 'んー' and not successive_bar(a + b + c + d + e):
                        print(a + b + c + d + e)
