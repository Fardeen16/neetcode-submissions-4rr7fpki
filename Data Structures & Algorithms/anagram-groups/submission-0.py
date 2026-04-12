class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs:
            temp = [0] * 26

            for j in i:
                temp[ord(j) - ord("a")] += 1

            ans[tuple(temp)].append(i)

        return ans.values() 




