'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    seen = {}
    for i in range(len(arr)):
        if arr[i] in seen:
            del seen[arr[i]]
        else:
            seen[arr[i]] = arr[i]
    return next(iter(seen.values()))


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

#     def __str__(self):
#         return f'{self.value}'

#     def find_middle(self): # Time: O(n), Space: O(1)
#         count = 0
#         current_mid = self
#         current_node = self
#         while current_node.next is not None:
#             if count is 1:
#                 current_mid = current_mid.next
#                 count = 0
#             else:
#                 count += 1
#             current_node = current_node.next
#         return current_mid


# root = Node(3)
# root.next = Node(4)
# root.next.next = Node(5)
# root.next.next.next = Node(6)
# root.next.next.next.next = Node(7)
# root.next.next.next.next.next = Node(8)

# print(root.find_middle())