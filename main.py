from hashlib import new
import os
import fnmatch
import csv
from tokenize import Number

files_names_list = []

for file_name in os.listdir("test_files"):
    if fnmatch.fnmatch(file_name, "*.csv"):
        files_names_list.append(file_name)

print(files_names_list)

users_files_object = {

}


class FileQuiz:
    def __init__(self, file_route: str) -> None:

        self.__file_route = file_route

    def getQuiz(self):
        with open(f"test_files/{self.__file_route}", encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            quiz = []

            for user_row in csv_reader:
                user_row_data = {"firstname": user_row["First Name"], "lastname": user_row["Last Name"], "score": int(
                    user_row["Score"])}

                quiz.append(user_row_data)

            return quiz


def counter_test(parameter):
    counter = 0
    list_test = []

    for number in range(len(parameter)):
        new_list = FileQuiz(parameter[counter])
        counter += 1

        list_test.append(new_list.getQuiz())
        # list_test.append("#################")

    return list_test


all_result = counter_test(files_names_list)

print(all_result)
