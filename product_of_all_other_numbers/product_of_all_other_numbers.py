'''
Input: a List of integers
Returns: a List of integers
'''
import math
def product_of_all_other_numbers(arr):
    # make a new array
        # for each item in range of array

    t = []
    for i in range(len(arr)):
        t.append(math.prod(arr[:i] + arr[i+1:]))
    # prod = []
    return t
    # for i in range(0, len(arr)): # moves the  compared index each time the nested for loop iterates through the array
    #     item = 1 #setting variable to be multiplied
    #     for j in range(0, len(arr)): #moves through the array, once it does, the i index is i+1 in the parent for loop
    #         if (j != i): # compares the i index with j to to determine if they do not equal eachother, then do the thing below it.
    #             item = item * arr[j] # multiply 1 by the index J
    #     prod.append(item)# append the multiplied item to the new array
    # return prod


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
