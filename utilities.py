import csv

def load_data(file_path):
    students_list = []

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students_list.append(row)
    return students_list