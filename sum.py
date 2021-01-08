class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        output = []
        for i in range(0, len(nums)):
            #print(len(nums))
            for j in range(1, len(nums)):
                print(len(nums))
                print("j value " + str(j))
                print("i value " + str(i))
                x = nums[i] + nums[j]
                print("x value" + str(x))
                if x == target and i != j :
                    output.append(i)
                    output.append(j)
                    return output
