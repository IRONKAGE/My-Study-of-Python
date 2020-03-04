# Приклад №1 - перетин кіл (у масиві)

# radius= [[4, 5, 6, 9, 1, 3, 1], [6, 30, 5, 1, 7, 9]]
# resultat = set(radius[0])

# for item in radius:
#     resultat = resultat.intersection(item)

# print(resultat)



# Приклад №2 - перетин кіл (у списках)

# radius_1 = {4, 5, 6, 9, 1, 3, 1}
# radius_2 = {3, 5, 1, 4, 3, 7, 2, 6}
# zitknennya = radius_1.intersection(radius_2)

# print(zitknennya)2

# Приклад №3 - перетин кіл у динамічній осі х (у масиві)

rm = [1, 5, 2, 1, 4, 0]

def solution(rm):
    events = []
    for i, a in enumerate(rm):
        events += [(i-a, +1), (i+a, -1)]
    events.sort(key=lambda x: (x[0], -x[1]))
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 10E6:
            return -1
    return intersections

print(solution(rm))

input('Натисніть ENTER для виходу')

