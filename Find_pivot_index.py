# find that element where lHS = RHS 
# means ak esa number jiske left side ki value ka sum uski right side ki value ke sum k brabar ho
def pivotIndex(arr):
    # Initialization:
    # Left hand side be empty, and
    # Right hand side holds all weights.
    total_weight_on_left = 0
    total_weight_on_right = sum(arr)

    for i, current_weight in enumerate(arr):

        total_weight_on_right -= current_weight

        if total_weight_on_left == total_weight_on_right:
                # balance is met on both sides
                # i.e., sum( nums[ :idx] ) == sum( nums[idx+1: ] )
            return i

        total_weight_on_left += current_weight

    return -1

arr = [1,7,3,6,5,6] # here 1+7+3 = 11 and 5+6 = 11 and answer is index of 6
print(pivotIndex(arr))