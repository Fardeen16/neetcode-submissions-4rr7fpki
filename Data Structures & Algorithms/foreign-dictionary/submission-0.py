class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # make an adjecency list t o map letter to next letter
        adj_list = {character: set() for word in words for character in word }
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])
                    break
            
        # initialize my variables
        visited_set = {}   # False -> Visited, TRUE -> In visiting Path
        result = []

        # the dfs logic to traverse the characters
        def is_there_cycle(character):
            if character in visited_set:
                return visited_set[character]
            
            visited_set[character] = True

            for nei in adj_list[character]:
                if is_there_cycle(nei):
                    return True

            visited_set[character] = False
            result.append(character)

        # run dfs on all characters in the adjecency list
        for each_char in adj_list:
            if is_there_cycle(each_char):
                return ""

        # reverse the result and return that  
        return "".join(result[::-1])