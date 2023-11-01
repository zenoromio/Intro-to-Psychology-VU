from typing import List, Dict


def create_grades_dict(filename: str) -> Dict[str, List[float]]:
    """This functions creates a dictonary from the txt file
    :param: filename: name of grades file
    :return: dictonary with studentname as key and a list of grade as value -> [test_grade, quizzes_grade, combined_grade]
    """

    grades: Dict[str, List[float]] = {}

    with open(filename, "r") as file:
        
        new_grade: List[float] = []
        new_student_nr: str = ""

        for index, line in enumerate(file):

            if len(line) == 8:

                if new_grade != []:
                    grades[new_student_nr] = new_grade

                new_student_nr = line.strip()
                new_grade: List[float] = []
            else:

                new_grade.append(float(line.strip()))

    return grades

grades_dict = create_grades_dict("grades_psych.txt")



def calculate_combined_mean(grades: Dict[str, List[float]]) -> float:
    """This functions calculate the mean of the combined grade
    :param: grades: dictonary with grades
    :return: mean of the combined grade
    """
    
    total_sum: float = 0.0
    count: int = 0

    for grade_list in grades.values():
        
        total_sum += grade_list[2]
        count += 1

    return round((total_sum / count), 2)

def calculate_test_mean(grades: Dict[str, List[float]]) -> float:
    """This functions calculate the mean of the test grade
    :param: grades: dictonary with grades
    :return: mean of the test grade
    """

    total_sum: float = 0.0
    count: int = 0

    for grade_list in grades.values():
        
        total_sum += grade_list[0]
        count += 1

    return round((total_sum / count), 2)

def calculate_quizzes_mean(grades: Dict[str, List[float]]) -> float:
    """This functions calculate the mean of the quizzes grade
    :param: grades: dictonary with grades
    :return: mean of the quizzes grade
    """

    total_sum: float = 0.0
    count: int = 0

    for grade_list in grades.values():
        
        total_sum += grade_list[1]
        count += 1

    return round((total_sum / count), 2)

def calculate_passed_failed(grades: Dict[str, List[float]]) -> str:
    """This functions calculate how many are passing and how many are failing
    :param: grades: dictonary with grades
    :return: message with number of passing and failing
    """

    passing: int = 0
    failing: int = 0

    for grade_list in grades.values():
        if grade_list[2] >= 5.5:
            passing += 1
        else:
            failing += 1

    message: str = f"""
        RESULTS OF TEST: \n
        Students passing: {passing}
        Students failing: {failing}
    """

    return message


#EXAMPLES

#print mean of quizzes
print(calculate_quizzes_mean(grades_dict))

#print passed and failed
print(calculate_passed_failed(grades_dict))





#code used to replace "," with "."
"""
with open("grades_psych.txt", "r") as file:
    
    data = file.read() 
  
    data = data.replace(",", ".")

with open("grades_psych.txt", "w") as file:
    file.write(data)
"""