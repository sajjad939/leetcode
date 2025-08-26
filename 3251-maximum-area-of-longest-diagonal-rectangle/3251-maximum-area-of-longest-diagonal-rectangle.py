class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
                maximum_diag=0
                area=0
                for l,w in dimensions:
                    current_diag=math.sqrt(l*l+w*w)
                    if current_diag>maximum_diag:
                            area=l*w
                            maximum_diag=current_diag
                    elif current_diag==maximum_diag:
                          area=max(area,l*w)
                return area

         
