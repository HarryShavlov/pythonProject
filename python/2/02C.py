#Юный программист Вася любит прогуливаться по тропинке длиной 
#D метров, проходящей неподалёку от его школы, и размышлять о том о сём.
#В начале прогулки Вася размышляет о Важных Вещах, и ноги несут его с постоянной скоростью, равной либо 
#v1, либо v2м/c. Затем Вася отвлекается и начинает думать о Всякой Ерунде. В этот момент его скорость становится равной либо 
#w1, либо w2 м/c.
#Если Вася затратил на прогулку T секунд, каково максимальное возможное расстояние, пройденное им с Важными Вещами в голове?

with open("input.txt") as f:
    d, t, v1, v2, w1, w2 = map(float, f.read().split())

answer = []

def calc_answer(v, w):
    if (v-w) != 0:
        answer = (d-w*t)/(v-w) * v
        if answer > 0 and answer <= d:
            return answer
    return 0.0

answer.append(calc_answer(v1, w1))
answer.append(calc_answer(v2, w2))
answer.append(calc_answer(v2, w1))
answer.append(calc_answer(v1, w2))

if d/v1 == t:
    answer.append(d)
if d/v2 == t:
    answer.append(d)
if ((d/w1 == t) and not((d/v1 !=t) or (d/v2 !=t))) or ((d/w2 == t) and not((d/v1 !=t) or (d/v2 !=t))):
    answer.clear()
    answer.append(0.0)

with open("output.txt", "w") as f:
    f.write(str(round(max(answer),4)))
