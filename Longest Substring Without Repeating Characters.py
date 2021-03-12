
"""
Seems like a dynamic programming problem

abcabcbb
12333321
pwwkew
121233

where res[i] is the longest sub-string ending at i.
"""

def length_longest_substring(s: str) -> int:
    # res = [0] * (len(s)+1)
    prev = 0
    max_substr = 0
    seen_ht = {}
    for i, letter in enumerate(s):
        distance_last_sighting = i + 0 - seen_ht.get(s[i], -1)
        curr = min(prev+1, distance_last_sighting)
        seen_ht[s[i]] = i
        max_substr = max(max_substr, curr)
        print(i, letter, distance_last_sighting, curr, prev, max_substr, seen_ht)
        prev = curr

    return max_substr


print(length_longest_substring("abcabcbb"))
print(length_longest_substring("qwertyu"))
print(length_longest_substring("pwwkew"))
