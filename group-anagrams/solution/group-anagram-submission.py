class Solution:
    def groupAnagrams(self,strs):
        anagrams_map={}
        for s in strs:
            sorted_word=''.join(sorted(s))
            if sorted_word in anagrams_map:
                anagrams_map[sorted_word].append(s)
            else:
                anagrams_map[sorted_word]=[s]
        return list(anagrams_map.values())

