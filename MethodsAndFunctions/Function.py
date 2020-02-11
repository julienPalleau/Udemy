
"My Solution"


def spy_game1(list):
    count = 0
    result = False
    for number in list:
        if (number == 0):
            count += 1
        elif ((count == 2) and (number == 7)):
            count += 1
            result = True

    return result


print(spy_game1([1, 2, 4, 0, 0, 7, 5]))
print(spy_game1([1, 0, 2, 4, 0, 5, 7]))
print(spy_game1([1, 7, 2, 0, 4, 5, 0]))

"Bootcamp udemy solution"
print("\n")


def spy_game2(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game2([1, 2, 4, 0, 0, 7, 5]))
print(spy_game2([1, 0, 2, 4, 0, 5, 7]))
print(spy_game2([1, 7, 2, 0, 4, 5, 0]))
