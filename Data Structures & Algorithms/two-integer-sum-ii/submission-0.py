class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []

        l=0
        r=len(numbers) - 1

        while l<r:
            sum = numbers[l] + numbers[r]

            if (sum<target):
                print('l+')
                l+=1
            elif (sum>target):
                print('r+')
                r-=1

            else:
                return [l+1, r+1]

        return ans



        