all_students = []
while True:
    print("\n--- University Admission Portal --- ") 
    name = input("Enter Name (or type 'Exit'to close): ")
    if name.lower() == 'exit':
        break

    else:
        dept = input("Enter Your Department: ").lower()
    try:
        marks = int(input("Enter Your Marks: "))
        student = {"name": name, "dept": dept, "marks": marks}
        if (dept == "engineering" or dept == "computer"):
            if marks >= 70:
                student["status"] = "Approved: You Meet The 70% Merit For The Tech Programs,"
            else:
                diff = 70 - marks
                student["status"] = f"Rejected: You Need {diff} More Marks For {dept}."
        elif dept == "medical":
         if marks >= 80:
              student["status"] = "Approved: Congratulations! You Cleared The 80% Medical Threshold."
         else:
              diff = 80 - marks
              student["status"] = f"Rejected: Short By {diff} Marks For Medical."
        else:
         student["status"] = "Error: Department Not Recognized."
    
        all_students.append(student)
        print(f"Record Saved For: {name}!")
    except ValueError:
        print("Invalid Marks! Try Again.")
        print("\n--- All Registered Students ---")
for s in all_students: 
     print(f"Name: {s['name']} | status: {s['status']}")


 
    