class multipleFunctions():
    def Subfields():
        list1 = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Processing Language"]
        print("Sub-fields in AI are: \n")
        for lst1 in list1:
            print(lst1, end="\n")
            
    def OddEven():
        input_number = int(input("Enter the number: "))
        if (input_number % 2) == 0:
            print(f"{input_number} is Even number")
        else: 
            print(f"{input_number} is Odd number")

    def Eligibile():
        gender = str(input("Your Gender: ").lower())
        age = int(input("Your age: "))
        if gender not in ["male","female"]:
            return "Input Gender is not valid. Please input gender as male or female."
        if gender == "male":
            if age > 21:
                return "Eligible"
            else:
                return "Not Eligible"
        elif gender == "female":
            if age > 18:
                return "Eligible"
            else:
                return "Not Eligible"

    def percentage():
        subject1 = int(input("Subject1= "))
        subject2 = int(input("Subject2= "))
        subject3 = int(input("Subject3= "))
        subject4 = int(input("Subject4= "))
        subject5 = int(input("Subject5= "))
        total = subject1+subject2+subject3+subject4+subject5
        percent = total/5
        data = f"Total : {total}, Percentage: {percent}"
        return data

    def triangle():
        height_area = int(input("Enter the height to calculate Area of triangle: "))
        breadth_area = int(input("Enter the breadth_area to calculate Area of triangle: "))
        height1_perimeter = int(input("Enter the height1 to calculate perimeter of triangle: "))
        height2_perimeter = int(input("Enter the height2 to calculate perimeter of triangle: "))
        breadth_perimeter = int(input("Enter the breadth to calculate perimeter of triangle: "))

        area = ((height_area * breadth_area) / 2)
        perimeter = (height1_perimeter + height2_perimeter + breadth_perimeter)

        print("Area Formula: (Height*Breadth)/2\nArea of Triangle: ", area, "\nPerimeter formula: Height1+Height2+Breadth\nPerimeter of Triangle: ", perimeter)