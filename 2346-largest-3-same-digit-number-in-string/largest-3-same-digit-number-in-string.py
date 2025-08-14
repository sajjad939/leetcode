class Solution:
    def largestGoodInteger(self, num: str) -> str:
     sum_digit_number=["999","888","777","666","555","444","333","222","111","000"]   
     for good_integer in sum_digit_number:
        if good_integer in num:
            return good_integer
     return ""