for i in range(1,100):
    print("Hello World")

def cal_avg():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    third_num = int(input("Enter third number: "))
    avg = (first_num + second_num + third_num) / 3
    print("The average of the three numbers is:", avg)

cal_avg()