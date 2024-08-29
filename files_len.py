def read_file_info(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        return file_name, line_count, lines


files_to_read = ['1.txt', '2.txt', '3.txt']

file_info_list = []

for file_name in files_to_read:
    info = read_file_info(file_name)
    file_info_list.append(info)

file_info_list.sort(key=lambda x: x[1])


def write_combined_file(sorted_file_info, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for fileName, line_count, lines in sorted_file_info:
            outfile.write(f"{fileName}\n{line_count}\n")
            outfile.writelines(lines) # <----------------------------- Текст записывается супер-коряво не знаю как исправить


output_filename = 'combinator_texts.txt'
write_combined_file(file_info_list, output_filename)