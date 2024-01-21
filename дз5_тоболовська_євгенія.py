# -*- coding: utf-8 -*-
"""ДЗ5_Тоболовська Євгенія.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDwGS0tbHhn8dBThFqdGHeFvoZArIsYS

Завдання 1
"""

class HashTable:
    # ... Інші частини класу HashTable ...

    def delete(self, key):
        """Видаляє пару ключ-значення за заданим ключем."""
        hash_key = self._hash_function(key)
        key_exists = False
        bucket = self.array[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print(f"Пара ключ-значення для ключа '{key}' видалена.")
        else:
            print(f"Ключ '{key}' не знайдено.")

    # ... Решта методів класу HashTable ...

"""Завдання 2"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        mid_value = arr[mid]

        if mid_value == target:
            # Знайдено точне значення, верхня межа знайдена
            upper_bound = mid_value
            break
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = mid_value  # Поточне значення є потенційною верхньою межею

    # Якщо верхня межа не знайдена, значить всі елементи менші за цільове значення
    if upper_bound is None:
        upper_bound = -1  # Або встановлюємо інше значення, що вказує на відсутність верхньої межі

    return (iterations, upper_bound)

# Тестування функції
sorted_array = [0.5, 1.2, 1.5, 2.3, 3.6, 4.1, 5.8]
target_value = 2.5
binary_search(sorted_array, target_value)

"""Завдання 3"""

# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    def build_last(pattern):
        last = [-1] * 256
        for i in range(len(pattern)):
            last[ord(pattern[i])] = i
        return last

    last = build_last(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1

    if i > n - 1:
        return -1

    j = m - 1
    while True:
        if pattern[j] == text[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            last_occurrence = last[ord(text[i])]
            i = i + m - min(j, 1 + last_occurrence)
            j = m - 1
            if i > n - 1:
                break
    return -1

# Реалізація алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern, d=256, q=101):
    M = len(pattern)
    N = len(text)
    h = 1
    p = 0
    t = 0

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            match = True
            for j in range(M):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q
    return -1

# Приклад використання
text = "this is a simple example"
pattern = "example"

# Використання алгоритмів
bm_result = boyer_moore_search(text, pattern)
kmp_result = knuth_morris_pratt_search(text, pattern)
rk_result = rabin_karp_search(text, pattern)

bm_result, kmp_result, rk_result

# Виправлений шлях до файлів
file_path_article1 = 'https://drive.google.com/file/d/1lZpNfDl74_Ri-gcFntxrAokLIrFwYccL/view?usp=sharing'
file_path_article2 = 'https://drive.google.com/file/d/12qLg1pTdvYnJ3H4k9Mxo713sPnG3g05N/view?usp=sharing'

# Зчитування тексту з файлів
text_article1 = read_text_from_file(file_path_article1)
text_article2 = read_text_from_file(file_path_article2)

# Вимірювання часу для кожного алгоритму на кожній статті знову
times = {}
for article, text in [('article1', text_article1), ('article2', text_article2)]:
    for pattern in [existing_substring, non_existing_substring]:
        for search_function in [boyer_moore_search, knuth_morris_pratt_search, rabin_karp_search]:
            time = measure_time(text, pattern, search_function)
            times[(article, pattern, search_function.__name__)] = time

times

"""На основі проведених вимірювань часу виконання, можна зробити наступні висновки щодо швидкості трьох алгоритмів пошуку підрядків (Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа) для двох текстів:

Для першої статті ("Використання алгоритмів у бібліотеках мов програмування"):

Алгоритм Боєра-Мура виявився найшвидшим як для існуючого підрядка (0.00307 секунди), так і для невідомого підрядка (0.00153 секунди).
Для другої статті ("Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі"):

Алгоритм Боєра-Мура також показав найкращі результати, з часом виконання 0.00284 секунди для існуючого підрядка та 0.00188 секунди для невідомого підрядка.
Отже, для обох текстів найшвидшим алгоритмом виявився алгоритм Боєра-Мура. Це може бути пов'язано з ефективністю цього алгоритму у випадках, коли підрядок рідко зустрічається у тексті, а також із його здатністю "пропускати" непотрібні частини тексту.

Алгоритми Кнута-Морріса-Пратта та Рабіна-Карпа виявилися повільнішими у порівнянні з Боєром-Муром у даному тесті, що може бути обумовлено їх внутрішньою структурою та підходом до пошуку підрядків.

Висновки щодо швидкостей алгоритмів пошуку підрядка

Алгоритми:
Боєр-Мур
Кнут-Морріс-Пратт
Рабін-Карп

Тексти для аналізу:
Стаття 1: "Використання алгоритмів у бібліотеках мов програмування"
Стаття 2: "Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі"

Швидкість алгоритмів:

Стаття 1:

Боєр-Мур:
Існуючий підрядок: 0.00307 сек
Невідомий підрядок: 0.00153 сек
Кнут-Морріс-Пратт:
Існуючий підрядок: 0.01068 сек
Невідомий підрядок: 0.01117 сек
Рабін-Карп:
Існуючий підрядок: 0.01364 сек
Невідомий підрядок: 0.01299 сек

Стаття 2:

Боєр-Мур:
Існуючий підрядок: 0.00284 сек
Невідомий підрядок: 0.00188 сек
Кнут-Морріс-Пратт:
Існуючий підрядок: 0.02423 сек
Невідомий підрядок: 0.02450 сек
Рабін-Карп:
Існуючий підрядок: 0.01854 сек
Невідомий підрядок: 0.01907 сек

Генеральні висновки:
Алгоритм Боєра-Мура виявився найшвидшим у пошуку як існуючих, так і невідомих підрядків у обох статтях.
Алгоритм Кнута-Морріса-Пратта і Рабіна-Карпа показали повільніші результати порівняно з Боєром-Муром. Це може бути обумовлено їх внутрішньою структурою та способом обробки тексту.
Боєр-Мур ефективний у випадках, коли підрядок рідко зустрічається у тексті або коли є можливість "пропустити" значні частини тексту під час пошуку.

Застосування результатів:
Вибір алгоритму для практичних цілей слід базувати на конкретних вимогах до швидкості та характеристик тексту.
Боєр-Мур є відмінним вибором для загальних задач пошуку підрядків, зокрема, коли потрібна висока швидкість обробки великих обсягів тексту.
"""