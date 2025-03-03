
file = open('input_2.txt', 'r')
lines = file.readlines()
file.close()

safe_count = 0

def is_safe(report):
    increasing = True
    decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:  
            decreasing = False
        if report[i] > report[i + 1]:  
            increasing = False
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False  
    
    return increasing or decreasing

for line in lines:
    report = list(map(int, line.split()))
    
    if is_safe(report):
        safe_count += 1

print("Number of safe reports:", safe_count)

#Result: 218