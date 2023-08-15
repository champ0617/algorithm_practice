from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        for i in range(len(citations)):
            if citations[i] <= h_index:
                continue

            count = 0
            for j in range(len(citations)):
                if citations[j] >= citations[i]:
                    count += 1
            h_index = max(h_index, min(count, citations[i]))
        return h_index

if __name__ == "__main__":
    citations = [3,0,6,1,5]
    print(Solution().hIndex(citations))
