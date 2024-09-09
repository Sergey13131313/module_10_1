import time
from threading import Thread


def wite_words(word_count, file_name):
    for i in range(word_count):
        print(f'Какое-то слово № {i}')
        time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end_time = time.time()
print(f'Работа потоков {round(end_time - start_time, 2)}')

start_time = time.time()

thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()


end_time = time.time()
print(f'Работа потоков {round(end_time - start_time, 2)}')
