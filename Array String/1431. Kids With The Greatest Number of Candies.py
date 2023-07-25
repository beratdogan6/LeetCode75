class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []
        for i in candies:
            if (i + extraCandies) >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        return result
