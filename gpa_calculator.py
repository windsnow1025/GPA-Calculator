import json
from typing import Any

GPAScaleRules = list[dict[str, float]]
GPAScales = dict[str, GPAScaleRules]
Courses = list[dict[str, Any]]
SemesterCourses = list[Courses]
Semesters = list[str]


def load_gpa_scales() -> GPAScales:
    with open('gpa_scales.json', 'r') as f:
        return json.load(f)


def score_to_gpa(score: float, scale_rules: GPAScaleRules) -> float:
    for rule in scale_rules:
        if rule['min'] <= score <= rule['max']:
            return rule['gpa']
    return 0


def calculate_weighted_averages(
        courses: Courses,
        scale_rules: GPAScaleRules
) -> dict[str, float]:
    total_credit_score = sum(course['credit'] * course['score'] for course in courses)
    total_credit_gpa = sum(course['credit'] * score_to_gpa(course['score'], scale_rules) for course in courses)
    total_credit = sum(item['credit'] for item in courses)

    if total_credit == 0:
        return {'avg_score': 0, 'avg_gpa': 0}

    avg_score = total_credit_score / total_credit
    avg_gpa = total_credit_gpa / total_credit

    return {'avg_score': avg_score, 'avg_gpa': avg_gpa}
