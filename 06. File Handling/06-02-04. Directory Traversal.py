# 06-02. File Handling - Exercise
# 04. Directory Traversal

import os


def get_report_info(directory, folder):
    report_info_ = {}
    for root, dirs, files in directory:
        if folder in root:
            for f in files:
                file_name, file_extension = os.path.splitext(f)
                if file_extension not in report_info_:
                    report_info_[file_extension] = []
                report_info_[file_extension].append(f)
    return report_info_


path = os.walk(os.path.dirname(os.path.abspath(__file__)))
output = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'report.txt')

report_info = get_report_info(path, 'Example')

with open(output, "w") as file:
    for key, values in sorted(report_info.items(), key=lambda x: (x[0], x[1])):
        file.write(f"{key}\n")
        for value in values:
            file.write(f"- - - {value}\n")
