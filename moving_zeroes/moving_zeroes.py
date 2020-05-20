'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr): # Time: O(n) Space: O(n)
    # Your code here
    no_zeros = [i for i in arr if i is not 0]
    num_zeros = len(arr) - len(no_zeros)
    no_zeros.extend([0] * num_zeros)
    return no_zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")