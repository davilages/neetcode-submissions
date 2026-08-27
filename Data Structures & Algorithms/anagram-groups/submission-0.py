class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        anagrams = []
        index = 0
        for string in strs:
            key = tuple(sorted(string))
            if key not in seen:
                seen[key] = index
                anagrams.append([string])
                index += 1
            else:
                anagrams[seen[key]].append(string)
        return anagrams