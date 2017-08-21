def maxArea(heights):
        """
        :type heights: List[int]
        Given a list of wall heights, where heights[i] = j indicates that there
        is a wall of heights j at x = i, return the max inner area created by two
        walls within heights, i.e. the pair of walls that would hold the most water.
        """
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            max_area = max(max_area, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
