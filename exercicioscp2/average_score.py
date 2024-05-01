def calculate_average_score(*grades):
    total_score = 0
    for grade in grades:
        total_score += grade

    print(f'{total_score=}')
    print(f'{len(grades)=}')

    return total_score / len(grades)


print(calculate_average_score(80, 90, 100))
