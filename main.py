from student import StudentInfo
from search import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from mainmenu import MainMenu 

stu = StudentInfo()
searcher, addstu, printAll = SearchStudent(stu), AddStudent(stu), PrintAllStudent(stu)
main = MainMenu (searcher, addstu, printAll)

#call the list in data in file
stu.read()

main.login()