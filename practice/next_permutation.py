def next_permutation(nums):
    # 1)i is a pivot indicating first pair where asc order no longer true
    i = len(nums)-2
    while i>=0 and nums[i+1] > nums[i]:
        i-=1
    
    # 2) find the lowest number from the right that is higher than the pivot number
    j = len(nums)-1
    while nums[j]<=nums[i]:
        j-=1
    nums[i],nums[j]=nums[j],nums[i]
    
    left,right = i+1,len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1

nums = [1,2,4,3,6]
next_permutation(nums)