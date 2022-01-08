def findDuplicate(nums):
    output = []
    for num in nums:
        print("num: ",num)
        if nums[abs(num) - 1] < 0:
            output.append(abs(num))
            print("output",output)
            
        else:
            nums[abs(num) - 1] *= -1
            print(nums)
    return output

arr = [1,2,1,4]
print(findDuplicate(arr))

'''def findDuplicates(self, nums: List[int]) -> List[int]:

    uniques = set()
    dublicates = []

    while nums:
        num = nums.pop()
        print("pop",num)
        if num not in uniques:
            uniques.add(num)
            print("unique",uniques)
        else:
            dublicates.append(num)

    return dublicates'''