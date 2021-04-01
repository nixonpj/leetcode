"""
Given an array of strings strs, group the anagrams together. You can
return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""
from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = [[strs[0]]]
        counts_groups = [Counter(strs[0])]

        for word in strs[1:]:
            word_count = Counter(word)
            found = False
            for i, group_count in enumerate(counts_groups):
                if word_count == group_count:
                    anagram_groups[i].append(word)
                    found = True
            if not found:
                anagram_groups.append([word])
                counts_groups.append(word_count)
        return anagram_groups

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = [sorted(word) for word in strs]
        counts_groups = [Counter(strs[0])]

        for word in strs[1:]:
            word_count = Counter(word)
            found = False
            for i, group_count in enumerate(counts_groups):
                if word_count == group_count:
                    anagram_groups[i].append(word)
                    found = True
            if not found:
                anagram_groups.append([word])
                counts_groups.append(word_count)
        return anagram_groups




s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))