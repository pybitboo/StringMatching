from StringMatching.matcher import BruteForce

s = 'abcabdddabcab'
p = 'abc'

bf = BruteForce(p)

matches = bf.match(s)
print(matches)
