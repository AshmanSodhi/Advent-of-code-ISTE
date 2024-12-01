from collections import Counter

def split_numbers(input_file, list1, list2):
    with open(input_file, 'r') as iff, \
         open(list1, 'w') as lf, \
         open(list2, 'w') as rf:
        
        for line in iff:
            numbers = line.split()
            if len(numbers) == 2:
                lf.write(numbers[0] + '\n')
                rf.write(numbers[1] + '\n')

def read_and_sort(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    numbers.sort()
    return numbers

def total_distance(list1, list2):
    total_dist = 0

    for left_num, right_num in zip(list1, list2):
        total_dist += abs(left_num - right_num)
    
    return total_dist

def calculate_similarity_score(list1, list2):
    right_counts = Counter(list2)
    
    similarity_score = 0
    
    for number in list1:
        count_in_right = right_counts.get(number, 0)
        similarity_score += number * count_in_right
    
    return similarity_score

input_file = 'input.txt'
list1 = 'list1.txt'
list2 = 'list2.txt'
split_numbers(input_file, list1, list2)

list1_sort = read_and_sort(list1)
list2_sort = read_and_sort(list2)

total_distance = total_distance(list1_sort, list2_sort)
print("Total distance:", total_distance)

similarity_score = calculate_similarity_score(list1_sort, list2_sort)
print("Similarity score:", similarity_score)


