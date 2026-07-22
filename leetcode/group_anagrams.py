class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        words_anagrams = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key not in words_anagrams:
                words_anagrams[key] = []
            words_anagrams[key] += [words]

        return list(words_anagrams.values())