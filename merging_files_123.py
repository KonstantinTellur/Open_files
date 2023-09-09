import os
file_list = ['exercise_1.txt', 'exercise_2.txt', 'exercise_3.txt']
exercise_file_list = ['n_exercise_1.txt', 'n_exercise_2.txt', 'n_exercise_3.txt']
exercise_data_from_files = []
step = 0
while step < len(file_list):
    for some_file in file_list:
        with open(file_list[step], encoding='UTF-8') as f:
            data = f.readlines()
            qvon_str = len(data)
        with open(file_list[step], encoding='UTF-8') as f:
            data_text = f.read()

    for some_file in exercise_file_list:
        with open(exercise_file_list[step], 'w') as f:
            f.write(f'{file_list[step]}\n')
            f.write(f'{qvon_str}\n')
            f.write(f'{data_text}\n')
            step += 1
    for some_file in exercise_file_list:
        with open(some_file) as f:
            exercise_data = f.read()
            exercise_data_from_files.append(exercise_data)
exercise_data_from_files.sort(key=len)
sorted(exercise_data_from_files, key=len)
with open('finish_file.txt', 'r', encoding='cp1251') as f:
    print(f.read())
print(exercise_data_from_files)
          