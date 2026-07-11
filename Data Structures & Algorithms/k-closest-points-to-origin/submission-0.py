class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        return self._KClosest(points, 0, len(points)-1)[:k]

    def _KClosest(self, points, s, e):
        if e-s+1 <= 1:
            return points

        #sqrt((x1 - x2)^2 + (y1 - y2)^2)

        pivot = (points[e][0])**2 + (points[e][1])**2
        left = s

        for i in range(s, e):
            distancei = (points[i][0])**2 + (points[i][1])**2
            if distancei < pivot:
                points[i], points[left] = points[left], points[i]
                left += 1

        points[e], points[left] = points[left], points[e]

        self._KClosest(points, s, left-1)
        self._KClosest(points, left+1, e)

        return points
