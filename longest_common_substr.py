from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    res = strs[0]
    for i in range(len(res)):
        for word in strs:
            try:
                if word[i] != res[i]:
                    return res[:i]
            except IndexError:
                return res[:i]
    return res


print(longest_common_prefix(["flow", "flowe", "floweight"]))
