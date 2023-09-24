class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [poured]
        for _ in range(query_row):
            nxt = [0]*(len(glasses)+1)
            for key, value in enumerate(glasses):
                if value <= 1:
                    continue
                move = (glasses[key]-1)/2.0
                nxt[key] += move
                nxt[key+1] += move
                glasses[key] = 1
            glasses = nxt
        return min(1, glasses[query_glass])