class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            tar_x, tar_y = points[i+1]
            # the determining factor for the total_time is going to be what the greatest difference is between the two points.
            total_time += max(abs(curr_x - tar_x), abs(curr_y - tar_y))
        return total_time

