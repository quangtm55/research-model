file = open("Book1.csv", mode= "r")
new_file = open("NewBook1.csv", mode= "w")



header = file.readline()
new_file.write(header.strip("\n") + ",BMI" + ",Size base on BMI")
next_row = file.readline()
while next_row != "":
    
    next_row_list = next_row.split(",")

    height = float(next_row_list[0])
    height_meter = height/100
    weight = float(next_row_list[1])

    bmi = float(weight)/(height_meter*height_meter)
    bmi = round(bmi, 2)

    if height >= 165:
        size = "L"
    elif bmi >= 24 and height < 165:
        size = "L"
    else:
        size = "M"

    new_row = " \n" + next_row.strip("\n") + "," + str(bmi) + "," + size
    new_file.write(new_row)
    
    next_row = file.readline()
    

