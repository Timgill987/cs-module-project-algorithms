'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #need to be able to change the index of any existing zeros in a given array
    #need to use a method that can manipulate the index value for list items

    # if value is equal to 0
        # any 0's index is +1
        for i in arr:
            if i == 0:
                arr.remove(0)
                arr.append(0)
        return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")