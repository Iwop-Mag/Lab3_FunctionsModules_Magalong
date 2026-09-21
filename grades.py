def compute_average(scores):
    return sum(scores) / len(scores)

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def generate_remark(grade):
    remarks = {
        "A": "Excellent Performance",
        "B": "Good Performance",
        "C": "Satisfactory Performance",
        "D": "Needs Improvement",
        "F": "Failing Status"
    }
    return remarks.get(grade, "Invalid Grade")