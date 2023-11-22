data = ['Hubert Madej', 'UEK', 'Applied Informatics']

file = open(r'during/student.txt', 'w')

for i in data:
    file.write(i+'\n')

file.close()