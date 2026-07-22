class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq = {}
        max_val = []
        final = []

        for integers in nums:
            if integers not in freq.keys():
                freq[integers] = 1

            else:
                freq[integers] += 1
        

        max_val += (sorted(freq.keys(), key=lambda x: freq[x], reverse=True))

        for i in range(k):
            
            final.append(max_val[i])
              
        return final