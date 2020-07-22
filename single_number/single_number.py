'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #figure out a way to iterate through given array
    # figure out a way to filter out duplicate numbers

        #if the number exist once in the array
            #then display that number
        #else return
    for i in arr:
        if arr.count(i) == 1:
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")