import csv


def lower_snake_case(string: str) -> str:
    return str.lower(str(string)).replace(' ', '_')

def get_datas():
    content = []
    with open('datas/questions.csv', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            content.append(row)
        return sort_data(content)

#Never trust a csv file
def sort_data(content: list):
    matrice = {}
    for index, row in enumerate(content):
        if index == 0:
            continue
        use = lower_snake_case(row[2])
        subject = lower_snake_case(row[1])

        if use not in matrice.keys():
            matrice[use] = {}

        if subject not in matrice[use].keys():
            matrice[use][subject] = []
        matrice[use][subject].append(question_buidler(row))
    return matrice
    

def question_buidler(row: list):
    return {
        "question_text": str(row[0]),
        "answer": row[3],
        "answer_text": [
            str(row[4]),
            str(row[5]),
            str(row[6]),
            str(row[7])
        ],
        "remark": str(row[8])
    }

datas = get_datas()