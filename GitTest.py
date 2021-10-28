#Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся
# слов в файле, но через функции и map, без единого цикла!
print(list(map(lambda x: x*x, range(20))))
# file.readlines()
from sys import argv
# print(open(argv[0], 'r').readlines())
filename = "song"
file_io_wrapper = open(filename, "r")
L = file_io_wrapper.readlines()
my_dict = {i:L.count(i) for i in L}
print(my_dict)
file_io_wrapper.close()

# Нужно считать повторения через Лямбду