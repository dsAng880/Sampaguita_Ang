# DOMINIQUE JILLIAN S. ANG
# 8 - SAMPAGUITA
# STUDENT ID CHECKER

import re

student_id = input("Enter student ID: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("Student ID is valid")
else:
    print("Student ID is not valid")