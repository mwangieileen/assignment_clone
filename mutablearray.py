#Importing necessary libraries
import numpy as np
import array as array

student_names=np.array(["Alice", "Bob", "Charlie", "David", "Eva"])
print("Student Names:", student_names)

#Manipulating Arrays
#1- Editing Arrays
student_names[0]="Alicia"
print("Updated Student Names:", student_names)
student_names[3]="Laura"
print("Updated Student Names2:", student_names)

#Edits names from index 0 to 2-Just before index 3 and replaces them with new names
student_names[0:3]=["Rachael", "Robert", "Charles"]
print("Updated Student Names3:", student_names)


#2- Adding Arrays
#Adds new names to the end of the array
student_names=np.append(student_names,["David", "Eva"])
print("Updated Student Names4:", student_names)

#Adds new names to the beginning of the array/at a specific index
student_names=np.insert(student_names,0,["Alice", "Bob"])
print("Updated Student Names5:", student_names)

#Adds new name at index 3
student_names=np.insert(student_names,3,"Eileen")
print("Added new name at index 3",student_names)


#3- Deleting Arrays
#Deletes name at specific index
student_names=np.delete(student_names,0)
print("Deleted name at index 0:", student_names)
#Deletes specific name from the array
student_names=np.delete(student_names,np.where(student_names=="Rachael"))
print("Deleted name 'Rachael':", student_names) 
#Delete student name 'Eva' from the array
student_names=np.delete(student_names,np.where(student_names=="Eva"))
print("Deleted name 'Eva':", student_names)


#2D Array of Students' names and ages
students=np.array([
    ["Alice", 20],
    ["Bob", 21],
    ["Charlie", 22],
    ["David", 23],
    ["Eva", 24]
])
print(students)

#3D Array of Students' names and ages
students_3d=np.array([
    [
        ["Alice", 20],
        ["Bob", 21],
        ["Charlie", 22],
        ["David", 23],
        ["Eva", 24]
    ]
])
print(students_3d)

#Checking dimension of students 
print("Number of dimensions of students:", students.ndim)

#Checking dimension of students _3d
print("Number of dimensions of students_3d:", students_3d.ndim)

