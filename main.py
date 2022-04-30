from hashlib import new
import os
import fnmatch
import csv
from tokenize import Number

from pkg_resources import to_filename

files_names_list = []

for file_name in os.listdir("test_files"):
    if fnmatch.fnmatch(file_name, "*.csv"):
        files_names_list.append(file_name)


class FileQuiz:
    def __init__(self, file_routes: list[str]) -> list[str]:
        
        self.__file_routes = file_routes
        self.list_all_student = []

    def getQuiz(self):
        
        for each_file in self.__file_routes:
            
            with open(f"test_files/{each_file}", encoding='utf8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
            
                for user_row in csv_reader:
                    user_row_data = {"name_complete": user_row["First Name"].lower() + " " + user_row["Last Name"].lower(), "score": int(
                        user_row["Score"])}

                    self.list_all_student.append(user_row_data)

    # def getUserBestStudents(self, quantity_students: int) -> list[str]:
            


def format_text_in_list(text: str):
    formated_list = []
    
    if(" " in text):
        formated_list = text.split(" ")
    else:
        formated_list = text.split("_")
       
    return formated_list 




all_data = FileQuiz(files_names_list)
all_data.getQuiz()
# print(all_data.getUserBestStudents(4))

# print(all_data_list)


# asfasfasfafasfas
# fsaasfasfafafasfasf
# afassafasfsa


# final_lits_to_reduce = [{}, {}, {}]

# oredr_list = final_lits_to_reduce.(() => sore) 

# oreder_list[0, quantity_students -1]

# return final_list 