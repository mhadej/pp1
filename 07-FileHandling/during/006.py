movie_titles = ['Piła', 'Piła 2', 'Piła 3', 'Piła 4', 'Piła 5']

file = open(r'during/movies.txt', 'w', encoding="UTF-8")

for i in movie_titles:
    file.write(i + '\n')

file.close()