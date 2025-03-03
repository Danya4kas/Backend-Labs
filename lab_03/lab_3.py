def cal_value(line):
    digits = [char for char in line if char.isdigit()]
    if digits:
        return int(digits[0] + digits[-1])
    return 0

with open("input_3.txt", "r", encoding="utf-8") as file:
    total_sum = sum(cal_value(line) for line in file)

print(total_sum)

#Result: 55538