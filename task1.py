def main():
    student_marks = {
        'Ankit': 85,
        'Bina': 72,
        'Chinaye': 90,
        'Dipak': 68,
        'Piyush': 78
    }
    
    print("Student marks database created successfully!")
    student_name = input("\nEnter a student's name to find their marks: ")
    if student_name in student_marks:
        print(f"Marks for {student_name}: {student_marks[student_name]}")
    else:
        print(f"Sorry, no marks record found for student '{student_name}'")
if __name__ == "__main__":
    main()
