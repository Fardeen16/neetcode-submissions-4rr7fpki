class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for word in strs:
            mapp = [0]*26

            for c in word:
                mapp[ord(c) - ord("a")] += 1

            dictt[tuple(mapp)].append(word)
        
        return list(dictt.values())