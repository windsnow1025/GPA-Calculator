def grade_to_gpa(grade, scale=4.5):
    if scale == 4.5:
        if grade <= 59:
            return 0
        elif grade <= 64:
            return 1.0
        elif grade <= 69:
            return 1.5
        elif grade <= 74:
            return 2.0
        elif grade <= 79:
            return 2.5
        elif grade <= 84:
            return 3.0
        elif grade <= 89:
            return 3.5
        elif grade <= 94:
            return 4.0
        elif grade <= 100:
            return 4.5
    elif scale == 4.0:
        if grade <= 59:
            return 0
        elif grade <= 64:
            return 1.0
        elif grade <= 69:
            return 1.5
        elif grade <= 74:
            return 2.0
        elif grade <= 79:
            return 2.5
        elif grade <= 84:
            return 3.0
        elif grade <= 89:
            return 3.5
        elif grade >= 90:
            return 4.0


def calculate_weighted_averages(data, scale):
    total_credit_grade = sum(item['credit'] * item['grade'] for item in data)
    total_credit_gpa = sum(item['credit'] * grade_to_gpa(item['grade'], scale) for item in data)
    total_credit = sum(item['credit'] for item in data)

    if total_credit == 0:
        return {'average_grade': 0, 'average_gpa': 0}

    average_grade = total_credit_grade / total_credit
    average_gpa = total_credit_gpa / total_credit

    return {'average_grade': average_grade, 'average_gpa': average_gpa}
