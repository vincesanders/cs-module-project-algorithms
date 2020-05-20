'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k): # Time: O((n - k) * (k - 1)) Space: O(n)
    # Your code here
    solution = []
    for i in range(len(nums)): # O(n - k)
        if (i >= len(nums) + 1 - k):
            break
        max = nums[i]
        for j in range(1, k): # O(k - 1)
            if nums[i + j] > max:
                max = nums[i + j]
        solution.append(max)
    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
