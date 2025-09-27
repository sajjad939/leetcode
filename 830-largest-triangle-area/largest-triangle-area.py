class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(A,B,C):
            return abs(A[0]*(B[1]-C[1])+B[0]*(C[1]-A[1])+C[0]*(A[1]-B[1]))/2
        triples=combinations(points,3)
        MaxArea=0
        for triple in triples:
            MaxArea=max(MaxArea,area(*triple))
        return MaxArea
