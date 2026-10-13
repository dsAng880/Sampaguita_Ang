# DOMINIQUE JILLIAN S. ANG
# 8 - SAMPAGUITA
# STUDENT EVALUATOR


def display_header():
    title = "Student Performance Evaluator"

def student_info():
    info = input("Enter Student Name : ")
    score1 = input(int("Enter Student Score 1 : "))
    score2 = input(int("Enter Student Score 2 : "))
    score3 = input(int("Enter Student Score 3 : "))

def evaluate_performance(score1, score2, score3):
    total = score1 + score2 + score3
    average = total/3

    perf: if average == >90 and average == <=100: "Outstanding"
    if average == <90: ("Very Satisfactory")
    if average == <85: ("Satisfactory")
    if average == <80: ("Fairly Satisfactory")
    if average == <75: ("Needs Improvement")
    print("STUDENT PERFORMANCE REPORT")
    print("Average: ", average, perf)

def display_report():
    display_header()
    student_info()
    evaluate_performance()
