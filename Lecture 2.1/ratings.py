
best_rating = None
best_grade = None

with open('ratings.txt') as f:
    while True:
        grade = f.readline().strip()
        if not grade:
            break

        ratings = f.readline().strip()
        ratings_list = ratings.split()
        # ratings_int = []
        # for i in ratings_list:
        #     ratings_int.append(int(i))
        ratings_int = [int(i) for i in ratings_list]
        avg_ratings = sum(ratings_int)/len(ratings_int)

        f.readline()  # пустая строка

        if (best_rating is None) or (avg_ratings > best_rating):
            best_rating = avg_ratings
            best_grade = grade

        print('Класс {} со средней оценкой {}'.format(grade, avg_ratings))

    print('Лучший класс {} со средней оценкой {}'.format(best_grade, best_rating))
