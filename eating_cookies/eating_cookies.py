'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, c=None):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif c and c[n] > 0:
        return c[n]
    else:
        if not c:
            c = [0 for _ in range(n+1)]
        c[n] = eating_cookies(n-1, c) + eating_cookies(n-2, c) + eating_cookies(n-3, c)
    return c[n]
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



