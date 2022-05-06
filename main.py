import os
import fnmatch
import csv

files_names_list = []

for file_name in os.listdir("test_files"):
    if fnmatch.fnmatch(file_name, "*.csv"):
        files_names_list.append(file_name)

def format_text_in_list(text: str):
    formated_list = []

    if(" " in text):
        formated_list = text.split(" ")[0]
    #if("_" in text):
        #formated_list = text.split("_")
    #if("/" in text):
    #    formated_list = text.split("/")
    return formated_list

class FileQuiz:
    def __init__(self, file_routes: list[str]) -> list[str]:

        self.__file_routes = file_routes
        self.list_all_student = []

    def getQuizes(self):
        for each_file in range(len(self.__file_routes)):
    
            with open(f"test_files/{self.__file_routes[each_file]}", encoding='utf8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for user_row in csv_reader:
                    user_row_data = {"complete_name": user_row["First Name"].lower() +" " +  user_row["Last Name"].lower(), "Accuracy": str(user_row["Accuracy"]), "Score": int(user_row["Score"])}
                    self.list_all_student.append(user_row_data)
        #print(self.list_all_student)
        
    def getBestScoresStudents(self, quantity_students: int) -> list[str]:
        final_best_students = {}
        
        for student in self.list_all_student:
            if student["complete_name"] in final_best_students.keys():
                final_best_students[student["complete_name"]] += student["Score"]                
            else:
                final_best_students[student["complete_name"]] = student["Score"]
        
        final_best_students = sorted(final_best_students.items(), key=lambda item:item[1], reverse=True)
        
        for ordered_students in range(len(final_best_students)-(len(final_best_students)-quantity_students)):
            print(ordered_students+1, final_best_students[ordered_students])
    
    def getBestAccuracyStudents(self, percent_accuracy: int) -> list[str]:
        accuracy_formated = []
        
        for each_student in range(len(self.list_all_student)):
            #print(self.list_all_student[each_student])
            formated_info_acc = int(format_text_in_list(self.list_all_student[each_student]["Accuracy"]))
            #print(formated_info_acc)
            accuracy_formated.append({"complete_name": self.list_all_student[each_student]["complete_name"], "Accuracy":formated_info_acc})
        #print(accuracy_formated)
        
        final_accuracy_students = {}
        for student in accuracy_formated:
            if student["complete_name"] in final_accuracy_students.keys():
                final_accuracy_students[student["complete_name"]] += student["Accuracy"]               
            else:
                final_accuracy_students[student["complete_name"]] = student["Accuracy"]
        
        #print(final_accuracy_students)
        final_accuracy = []
        for each_student in final_accuracy_students:
            if final_accuracy_students[each_student]/len(files_names_list)>percent_accuracy:
                #print(final_accuracy_students[each_student])
                final_accuracy.append({"complete_name": each_student, "Accuracy": final_accuracy_students[each_student]/len(files_names_list)})
       
        accuracy_average_total = {}
        for student in final_accuracy:
            if student["complete_name"] in accuracy_average_total.keys():
                accuracy_average_total[student["complete_name"]] += student["Accuracy"]               
            else:
                accuracy_average_total[student["complete_name"]] = student["Accuracy"]
        
        accuracy_average_total = sorted(accuracy_average_total.items(), key=lambda item:item[1], reverse=True)
        
        for student in range(len(accuracy_average_total)):
            print(student+1, accuracy_average_total[student])
            

all_data = FileQuiz(files_names_list)
#qty_student_first_file = all_data.getQuiz() # get the students number from first file reviewed
all_data.getQuizes() # get the students number from first file reviewed
#print(qty_student_first_file)
all_data.getBestScoresStudents(int(input("Please, select the quantity the best students qualifications:" )))
all_data.getBestAccuracyStudents(int(input("Please, type the percent the best accuracy students:" )))
