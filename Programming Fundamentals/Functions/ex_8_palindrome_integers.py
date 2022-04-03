def palindrome(nums):
    for n in nums:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


numbers = list(input().split(', '))
palindrome(numbers)
