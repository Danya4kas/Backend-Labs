with open('input_1.txt') as file:
    array1, array2 = [], []
    for line in file:
        numbers = line.split()
        array1.append(int(numbers[0]))
        array2.append(int(numbers[1]))

sorted_array1 = sorted(array1)
sorted_array2 = sorted(array2)

result_sum = 0
for i in range(len(sorted_array1)):
    result_sum += abs(sorted_array1[i] - sorted_array2[i])

print("Count of all distances:", result_sum)

# extra task 
similarity_score = 0
for num in array1:
    count = array2.count(num)
    similarity_score += num * count

print("Similarity score:", similarity_score)


#Result: 1660292, extra_task = 22776016