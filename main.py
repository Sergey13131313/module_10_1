import time
from threading import Thread


def word(n) -> str:
    return f'Какое-то слово № {n}\n'


def wite_words(word_count, file_name):
    with open(file_name, mode="w") as f:
        for i in range(1, word_count + 1):
            w = word(i)
            f.write(w)
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_stop = time.time()

print(f'Работа потоков {time.strftime("%H:%M:%S", time.gmtime(time_stop - time_start))}')

tr_list = []
count_words = [10,30,200,100]

time_start = time.time()
for i in range(5, 9):
    filename = f'example{i}.txt'
    tr = Thread(target=wite_words, args=(count_words[i - 5], filename))
    tr_list.append(tr)

[tr.start() for tr in tr_list]
[tr.join() for tr in tr_list]
time_stop = time.time()

print(f'Работа потоков {time.strftime("%H:%M:%S", time.gmtime(time_stop - time_start))}')
