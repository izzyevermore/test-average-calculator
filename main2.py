# task 2
# Calculate a learners average mark

student_name = input("Please enter your name: ")
student_surname = input("Please enter your surname: ")

test1 = float(input("Please your mark for the first test: "))
test2 = float(input("Please enter your mark for the second test: "))
test3 = float(input("Please enter your mark for the third test: "))

def average_mark():

    average_mark = ((test1 + test2 + test3) / 3)

    if average_mark >= 50:
        print("You have passed!")

    if average_mark < 50:
        print("you have failed!")

    print("Your mark is " + str(average_mark) + "%")

average_mark()


from datetime import datetime, timedelta
now = datetime.now

for d in range(10):
    ten_date = now + timedelta(days=14)
    now = ten_date
    print(ten_date.strftime("%Y-%m-%d"))