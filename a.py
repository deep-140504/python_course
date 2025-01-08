def spy_game(nums):
    i = 0
    while i < len(nums) - 2:
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 1:
            return True
        i += 1
    return False
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))