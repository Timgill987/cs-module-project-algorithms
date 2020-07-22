'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # may need nested for loop
    # need to be able to evaluate 3 consecutive indexes in an array
    # need to be able to iterate that evaluation of 3 numbers alonge the length of the array
    max = 0
    maxarr = []
    for i in range(len(nums) - k + 1): # iterate through array to see the value in i-1 and i+1
        max = nums[i] #set max to index
        for j in range(1, k): # move window over array
            if nums[i + j] > max: # compare window numbers to the current max - if true then...
                max = nums[i + j] #assign max to the new highest number out of the window
        maxarr.append(max) #add determined highest number to maxxarr and do it again.
    return maxarr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3 #sets size of the window

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
