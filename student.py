class StudentInfo:
    def __init__(self):
        self.name, self.age, self.idnum, self.email, self.phone = "", "", "", "", ""
        self.allstudents = []
        

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIdNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIdNum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nID-number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}\n"
    
    def read(self):
        try:
            with open("data_student.txt", "r") as file:
                for line in file:
                # Split the line into individual fields
                    name, age, idnum, email, phone = line.strip().split(", ")
                # Create a new StudentInfo object
                    student = StudentInfo()
                    student.setName(name)
                    student.setAge(age)
                    student.setIdNum(idnum)
                    student.setEmail(email)
                    student.setPhone(phone)
                # Add the student object to allstudents list
                    self.allstudents.append(student)
            print("Data successfully read")
        except FileNotFoundError:
             print("File missing: data_student.txt")