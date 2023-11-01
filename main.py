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

def calculate_highest_combined_grade(grades: Dict[str, List[float]]) -> float:
    """This function calculates the highest grade
    :param: grades: dictonary with grades
    :return: highest grade
    """
    
    highest_grade: float = 0.0
    
    for grade_list in grades.values():
        if grade_list[2] > highest_grade:
            highest_grade = grade_list[2]

    return highest_grade

def calculate_lowest_combined_grade(grades: Dict[str, List[float]]) -> float:
    """This function calculates the lowest grade
    :param: grades: dictonary with grades
    :return: lowest grade
    """
    
    lowest_grade: float = 10
    
    for grade_list in grades.values():
        if grade_list[2] < lowest_grade:
            lowest_grade = grade_list[2]

    return lowest_grade

def calculate_median_combined_grade(grades: Dict[str, List[float]]) -> float:
    """This function calculates the median of combined grade
    :param: grades: dictonary with grades
    :return: median of combined grade
    """
    
    grades_list: List[float] = []

    for grade_list in grades.values():
        grades_list.append(grade_list[2])
    
    grades_list.sort()

    if len(grades_list) % 2 == 0:
        return grades_list[(len(grades_list) / 2)]
    else:
        num_up = (len(grades_list) + 1) / 2
        num_down = (len(grades_list) - 1) / 2
        median = (grades_list[int(num_down)] + grades_list[int(num_up)]) / 2

        return median



#EXAMPLES (print median grade)
print(calculate_median_combined_grade(grades_dict))


#code used to replace "," with "."
"""
with open("grades_psych.txt", "r") as file:
    
    data = file.read() 
  
    data = data.replace(",", ".")

with open("grades_psych.txt", "w") as file:
    file.write(data)
"""