class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        def check(a, b):
            agene = [*a]
            cnt = 0

            for i in range(0, len(agene)):
                if a[i] != b[i]:
                    cnt += 1

            if cnt != 1:
                return False
            return True

        q = deque([startGene])
        visited = {startGene}
        mut = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return mut

                for gene in bank:
                    res = check(cur, gene)
                    if res and (gene not in visited):
                        visited.add(gene)
                        q.append(gene)
            mut += 1

        return -1
