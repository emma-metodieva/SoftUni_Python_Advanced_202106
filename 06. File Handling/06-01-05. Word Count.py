# 06-01. File Handling
# 05. Word Count

import re


def get_file_content(path):
    with open(path, 'r') as data:
        data = ''.join(data.readlines())
        return pattern.findall(data.lower())


def write_to_file(data):
    for k, v in data:
        output_data = f'{k} - {v}'
        with open('Files/output.txt', 'a') as file:
            file.write(output_data)
            file.write("\n")


path_to_words = 'Lab Files/words.txt'
path_to_input = 'Lab Files/input.txt'

pattern = re.compile(r"[a-zA-Z\']+")

get_words = get_file_content(path_to_words)
get_text = get_file_content(path_to_input)

my_dict = {word: get_text.count(word) for word in get_words if word in get_text}
sorted_list = sorted(my_dict.items(), key=lambda x: -x[1])

write_to_file(sorted_list)
