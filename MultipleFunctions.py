class multipleFunctions:
    def Subfields():
        lists =["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print ("Sub-fields in AI are:")
        for list in lists:
            print (list)

    def OddEven():
        inputNum = int(input("Enter a number:"))
        if (inputNum%2==1):
            print ( inputNum,"is Odd number")
        else: 
            print ( inputNum,"is Even number")
            
    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if (age>20):
            print ("ELIGIBLE")
        else:
            print ("NOT ELIGIBLE")
    
    def percentage():
        subject1 = int(input("Subject1="))
        subject2 = int(input("Subject2="))
        subject3 = int(input("Subject3="))
        subject4 = int(input("Subject4="))
        subject5 = int(input("Subject5="))
        total=subject1+subject2+subject3+subject4+subject5
        percentage =  (total/500)*100
        print ("Total : ",total)
        print ("Percentage : ",percentage)
        
    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth="))
        print ("Area formula: (Height*Breadth)/2")
        area = (height*breadth)/2
        print ("Area of Triangle: ", area)

        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth="))
        print ("Perimeter formula: Height1+Height2+Breadth")
        perimeter =  height1+height2+breadth
        print ("Perimeter of Triangle: ",perimeter)        
