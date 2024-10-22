###
# Calculates the final grade for a test based
# on the number of points obtained
# Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points < 18 and points >= 14:
        grade = "Good"
    elif points <14 and points >=10:
        grade = "Satisfactory"
    else: 
        grade = "Fail"
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored 15 points on the test. Your final grade is {final_grade}')