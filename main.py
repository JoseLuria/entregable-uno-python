#from hashlib import new
import os
import fnmatch
import csv
#from tokenize import Number

from pkg_resources import to_filename

files_names_list = []

for file_name in os.listdir("test_files"):
    if fnmatch.fnmatch(file_name, "*.csv"):
        files_names_list.append(file_name)

def format_text_in_list(text: str):
    formated_list = []

    if(" " in text):
        formated_list = text.split(" ")
    if("_" in text):
        formated_list = text.split("_")
    #if("/" in text):
    #    formated_list = text.split("/")
    return formated_list

class FileQuiz:
    def __init__(self, file_routes: list[str]) -> list[str]:

        self.__file_routes = file_routes
        self.list_all_student = []

    def getQuiz(self):
        counter_student_first_file = 0
        for each_file in range(len(self.__file_routes)):
    
            with open(f"test_files/{self.__file_routes[each_file]}", encoding='utf8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for user_row in csv_reader:
                    user_row_data = {"name_complete": user_row["First Name"].lower() + " " + user_row["Last Name"].lower(), "score": int(
                        user_row["Score"])}

                    self.list_all_student.append(user_row_data)
                    if each_file == 0:
                        counter_student_first_file +=1
                        
        #print(self.list_all_student)
        return(counter_student_first_file)
        #print(counter_student_first_file)

    def getUserBestStudents(self, quantity_students: int) -> list[str]:
        final_best_students = []
        total_first_file = qty_student_first_file

        formated_name_student = []
        
        for each_student_index in range(len(self.list_all_student)):
            #    print(each_student_index, self.list_all_student[each_student_index])
            complete_names_and_score = []
            formated_name_student.append(format_text_in_list(self.list_all_student[each_student_index]["name_complete"]))
            #formated_name_student = format_text_in_list(self.list_all_student[each_student_index]["name_complete"])
            #print(each_student_index)
            #print(each_student_index, formated_name_student)
        #print(formated_name_student)
            if len(formated_name_student) > total_first_file:
                for complete_name_from_first_file in formated_name_student[each_student_index-total_first_file]:
                    coincidences= 0
                    #print(complete_name_from_first_file) # funciona ok
                #print(each_student_index-total_first_file) # funciona ok
                    for complete_name_next_file in formated_name_student[each_student_index]:
                        #print(complete_name_next_file)
                        #print("#################")    
                    #print(each_student_index-total_first_file) # funciona ok
                        if complete_name_from_first_file == complete_name_next_file:
                            coincidences += 1
                    #        print(coincidences)
                            if coincidences == 2:
                                complete_names_and_score.append({"numero_lista": each_student_index, "student": formated_name_student[each_student_index]})
                                #print(each_student_index, formated_name_student[each_student_index], (self.list_all_student[each_student_index]["score"]+self.list_all_student[each_student_index+total_first_file]["score"]))     
                        #    print("#################")    
                        #    print(complete_names_and_score)    
        #print(formated_name_student)
        #    #complete_names_and_score.append({"name_complete_formated": formated_name_student, "score":self.list_all_student[each_student_index]["score"]})
            #print(self.list_all_student[each_student_index]["name_complete_formated"])
            #return(self.list_all_student[each_student_index]["name_complete_formated"])
                
                
                
                
            #if len(complete_names_and_score) > total_first_file:
                #for each_part_complete_name in complete_names_and_score[each_student_index]["name_complete_formated"]: # funciona ok
                #    print(each_part_complete_name)# y esta linea imprime la linea anterior
            #        for part_complete_name_folowingFile in self.list_all_student[each_student_index]["name_complete"]:                
            #print( each_student_index, self.list_all_student[each_student_index])
        #print(complete_names_and_score)
                
            
        #print(self.list_all_student[each_student_index])
            
        #    for each_student_name in range(len(self.list_all_student)):
        #        var= self.list_all_student[each_student_name["name_complete"]]
        #        #formated_name_student = format_text_in_list(var)
        #        complete_name.append({"nombres": format_text_in_list(var), "score":self.list_all_student[each_student_name["score"]]})
        #print( each_student_index, self.list_all_student[each_student_name])
        


all_data = FileQuiz(files_names_list)
qty_student_first_file = all_data.getQuiz() # get the students number from first file reviewed
#print(qty_student_first_file)
all_data.getUserBestStudents(100)

# asfasfasfafasfas
# fsaasfasfafafasfasf
# afassafasfsa


# final_lits_to_reduce = [{}, {}, {}]

# oredr_list = final_lits_to_reduce.(() => sore)

# oreder_list[0, quantity_students -1]

# return final_list
