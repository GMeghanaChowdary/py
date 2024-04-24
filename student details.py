class Box:
   def __init__(self, currentName, currentRollNo, currentdbmsMarks, currentPythonMarks, currentCMarks, currentOSMarks, currentCNMarks):
       self.name = currentName
       self.rollNo = currentRollNo
       self.dbmsMarks = currentdbmsMarks
       self.pythonMarks = currentPythonMarks
       self.cMarks = currentCMarks
       self.osMarks = currentOSMarks
       self.cnMarks = currentCNMarks
      
   def printDetails(self):
       print(self.name, self.rollNo, self.dbmsMarks, self.pythonMarks, self.cMarks, self.osMarks, self.cnMarks)
      


student1 = Box("Harika", "5A1", 78, 67, 77, 89, 46)
student2 = Box("Swapna", "5A2", 38, 65, 97, 59, 41)
student3 = Box("Sushma", "5A3", 88, 95, 47, 89, 31)


student1.printDetails()
student2.printDetails()
student3.printDetails()
      
