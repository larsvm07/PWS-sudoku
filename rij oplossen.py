nums = [8, 3, 0, 5, 0, 0, 0, 9, 0]

uniques = []


def solve(row):
    for item in range(len(row)):
        value = row[item]
        if value == 0:
            value = 1
        elif value != 0 and value in uniques:
            print('unsolvable')
            exit
        while value in uniques:
            value += 1
            
        if value not in uniques:
            uniques.append(value)
            row[item] = value

if len(nums) > 9:
    print('too long')

elif len(nums) < 9:
    print('too short')
else:
    solve(nums)
    print(nums)
