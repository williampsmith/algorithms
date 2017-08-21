def maxArea(heights):
        """
        :type heights: List[int]
        Given a list of wall heights, where heights[i] = j indicates that there
        is a wall of height j at x = i, return the max inner area created by two
        walls within heights, i.e. the pair of walls that would hold the most water.
        """
        def calc_area(point1, point2):
            len = point2[0] - point1[0]
            return len * min(point1[1], point2[1])
        def reset_indices(i, j, heights):
            if heights[i] < heights[j]:
                return i + 1, j
            return i, j - 1

        heights_len = len(heights)
        if heights_len < 2:
            return 0

        points = zip(range(heights_len), heights)
        max_area = calc_area(points[0], points[-1])
        i, j = reset_indices(0, len(heights) - 1, heights)

        while i < j:
            temp_area = calc_area(points[i], points[j])
            if temp_area > max_area:
                max_area = temp_area
            i, j = reset_indices(i, j, heights)
        return max_area
