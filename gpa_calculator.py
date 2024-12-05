import json

def load_gpa_scales():
    with open('gpa_scales.json', 'r') as f:
        return json.load(f)

def grade_to_gpa(grade, scale_rules):
    for rule in scale_rules:
        if rule['min'] <= grade <= rule['max']:
            return rule['gpa']
    return 0

def calculate_weighted_averages(data, scale_rules):
    total_credit_grade = sum(item['credit'] * item['grade'] for item in data)
    total_credit_gpa = sum(item['credit'] * grade_to_gpa(item['grade'], scale_rules) for item in data)
    total_credit = sum(item['credit'] for item in data)

    if total_credit == 0:
        return {'average_grade': 0, 'average_gpa': 0}

    average_grade = total_credit_grade / total_credit
    average_gpa = total_credit_gpa / total_credit

    return {'average_grade': average_grade, 'average_gpa': average_gpa}