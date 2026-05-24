    
def get_students_with_score(score):
    result=[]
    for y in students:
        if y[1]==score:
            result.append(y[0])
    return result

if __name__ == '__main__':
    students=[]
    scores=[]
    for _ in range(int(input())):
        l1 = []
        name = input()
        score = float(input())
        scores.append(score)
        l1.append(name)
        l1.append(score)
        students.append(l1)
    scores = sorted(scores)
    scores = list(set(scores))
    secons_max_score = scores[1]
    result = get_students_with_score(secons_max_score)
    [print(x) for x in sorted(result, key=lambda x: x[0])]