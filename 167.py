class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        i = 0
        j = length-1

        while True:
            ls = []
            if numbers[i] + numbers[j] == target:
                ls.append(i+1)
                ls.append(j+1)
                return ls
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
