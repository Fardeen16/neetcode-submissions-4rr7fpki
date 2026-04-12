class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ''' 
        -> in case of a tie, lexicographically order should be returned
        -> there exists a valid pathway

        SO can do a DFS form JFK, ony append a destination in answer once it has no neighbour

        TC = 2.V^2 logV  

        '''

        # sort for lexo order 
        tickets.sort()

        # make an adjecency list for all flight paths
        adj_list = defaultdict(list)
        for source, destination in tickets:
            adj_list[source].append(destination)

        # get all variables
        visited_set = set()
        result = ["JFK"]

        # start dfs from JFK
        def dfs(airport):
            if len(result) == len(tickets)+ 1:
                return True
            
            if airport not in adj_list:
                return False

            temp = list(adj_list[airport])
            # check all neighbour
            for index, nei in enumerate(temp):
                adj_list[airport].pop(index)
                result.append(nei)

                if dfs(nei): return True

                adj_list[airport].insert(index, nei)
                result.pop()
            
        dfs("JFK")
        return result


        