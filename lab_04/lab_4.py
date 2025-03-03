with open('input_4.txt', 'r') as file:
    data = file.readlines()

def calculate_directory_size(dir_name):
    total_size = 0 
    result = 0  

    start_index = data.index(f"$ cd {dir_name}\n")
    data[start_index] = "$" 

    for i in range(start_index + 2, len(data)):
        parts = data[i].split() 

        if parts[0] == "$":
            break

        if parts[0] == "dir":
            subdir_result, subdir_size = calculate_directory_size(parts[1])
            total_size += subdir_size
            result += subdir_result

        if parts[0].isdigit():
            total_size += int(parts[0])

    if total_size <= 100000:
        result += total_size

    return result, total_size

result, _ = calculate_directory_size("/")
print("Sum of directory sizes ≤ 100000:", result)

#Result: 1453349