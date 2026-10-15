n= input("Please Enter Your Name: ")

str_seconds = input("Please Enter Your Seconds: ")
int_second = int(str_seconds)

hours = int_second // 3600
minutes = (int_second % 3600) // 60
seconds = int_second % 60

print(f"{n}, you have {hours} hours, {minutes} minutes, and {seconds} seconds to complete your task.")