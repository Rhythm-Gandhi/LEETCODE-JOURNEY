class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods starting from k
        seen = [False] * n
        queue = deque([k])
        seen[k] = True
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    queue.append(neighbor)
                    
        # Step 2: Check if any non-suspicious method invokes a suspicious one
        for u in range(n):
            if not seen[u]:
                for v in graph[u]:
                    if seen[v]:
                        return list(range(n))
                        
        # Step 3: Return the remaining non-suspicious methods
        return [i for i in range(n) if not seen[i]]