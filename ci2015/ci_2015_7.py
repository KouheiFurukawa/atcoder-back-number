from sys import stdin

S = stdin.readline().rstrip().split()

nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
        'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
        'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
        'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000
        }

ans = 0
local = 0
for i in range(len(S)):
    if nums[S[i]] == 100 or nums[S[i]] == 1000:
        ans += local * nums[S[i]]
        local = 0
    else:
        local += nums[S[i]]
    if i == len(S) - 1:
        ans += local

print(ans)
