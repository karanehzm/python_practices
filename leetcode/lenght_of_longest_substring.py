def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set() # to check for the subsetring
        first = 0 
        best = 0

        for index, c in enumerate(s):
            if c not in window:
                window.add(c)
                best = max(best, len(window))
            else:
                while(c in window):
                    window.remove(s[first])
                    first += 1 

                window.add(c)
                best = max(best, len(window))

        return best
