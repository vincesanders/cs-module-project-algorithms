'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr): # Time: O(2n) Space: O(1)
    # Your code here
    # find the product O(n)
    num_zeros = 0
    product = 1
    nonzero_product = 1
    for i in arr: # O(n)
        product *= i
        if i is 0:
            num_zeros += 1
        else:
            nonzero_product *= i
    if num_zeros > 1:
        for i in range(len(arr)): # O(n)
            arr[i] = 0
        return arr # total O(2n)
    # multiply each number by the product O(n)
    for i in range(len(arr)): # O(n)
        if product is 0 and arr[i] is not 0:
            arr[i] = 0
        elif product is 0 and arr[i] is 0:
            arr[i] = nonzero_product
        else:
            local_product = product // arr[i]
            arr[i] = local_product
    return arr # total O(2n)


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 7, 3, 4]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
