'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr): # Time: O(n^2) Space: O(1)
    # Your code here
    last_zero = 0
    for i in range(len(arr)):
        if arr[i] is 0:
            # add 0 to beginning
            arr[0] = 0
            # shift elements right
            for j in reversed(range(last_zero, i + 1)):
                arr[j] = arr[j - 1]
            last_zero += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")