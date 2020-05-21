from collections import deque
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k): # Time: O((n - k) * (k - 1)) Space: O(n)
    # Your code here
    # solution = []
    # for i in range(len(nums)): # O(n - k)
    #     if (i >= len(nums) + 1 - k):
    #         break
    #     max = nums[i]
    #     for j in range(1, k): # O(k - 1)
    #         if nums[i + j] > max:
    #             max = nums[i + j]
    #     solution.append(max)
    # O(n) attempt
    # max = 0
    # second_max = float('-inf')
    # for i in range(len(nums)): # O(n)
    #     if i < k:
    #         if nums[i] >= max:
    #             second_max = max
    #             max = nums[i]
    #         if i == k - 1:
    #             solution.append(max)
    #     else:
    #         if max is nums[i - k]:
    #             max = second_max
    #         elif second_max is nums[i - k]:
    #             second_max = nums[i]
    #         if nums[i] >= max:
    #             second_max = max
    #             max = nums[i]
    #         solution.append(max)
    solution = []
    q = deque() # allows O(1) removal from both ends of queue
    for i, n in enumerate(nums):        
        # remove elements from the Queue so long as the current number is greater that the element        
        while len(q) > 0 and n > q[-1]:
            q.pop()
        # add the number once all smaller numbers have been evicted from the Queue
        q.append(n)
        # calculate the window range
        window = i - k + 1
        # so long as the window's range == k, we'll add elements to the Queue
        if window >= 0:
            # add the max element, to the output List
            solution.append(q[0])
            # check if the number on the left side of the window is going to be 
            # evicted in the next iteration            
            # if it is, and if that value is at the front of the Queue, 
            # we need to evict it from the Queue            
            if nums[window] == q[0]:
                q.popleft()
    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
