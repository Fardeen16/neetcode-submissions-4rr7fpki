class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []

        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for nei in adj_list[node]:
                if dfs(nei):
                    return True
            visit[node] = False
            res.append(node)
            
        for c in adj_list:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        
            

            
