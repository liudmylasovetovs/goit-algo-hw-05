import requests
import timeit


# Функція для завантаження тексту з URL
def download_text(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None


# Функція для пошуку підрядка за допомогою алгоритму Бойера-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0 or m > n:
        return []

    last_occurrence = {pattern[i]: i for i in range(m - 1)}
    i = m - 1
    j = m - 1
    result = []

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                result.append(i)
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            last = last_occurrence.get(text[i], -1)
            i += m - min(j, 1 + last)
            j = m - 1

    return result


# Функція для пошуку підрядка за допомогою алгоритму Кнута-Морріса-Прата
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return []

    pi = [0] * m
    j = 0
    result = []

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            result.append(i - m + 1)
            j = pi[j - 1]

    return result


# Функція для пошуку підрядка за допомогою алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern):
    m, n = len(pattern), len(text)
    result = []

    if m == 0 or m > n:
        return result

    d = 256
    q = 101  # просте число

    h_pattern = h_text = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q

    for i in range(n - m + 1):
        if h_pattern == h_text:
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                result.append(i)

        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
            if h_text < 0:
                h_text += q

    return result


# Завантаження текстів статей
url_article1 = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
text_article1 = download_text(url_article1)

url_article2 = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"
text_article2 = download_text(url_article2)

# Підрядки для пошуку
pattern_exists = "Document Stores"
pattern_fake = "Що таке Soft Skills та чому вони важливі в ІТ сфері?"

# Вимірювання часу виконання для алгоритму Бойера-Мура
time_bm_article1_exists = timeit.timeit(lambda: boyer_moore_search(text_article1, pattern_exists), number=1000)
time_bm_article1_fake = timeit.timeit(lambda: boyer_moore_search(text_article1, pattern_fake), number=1000)

time_bm_article2_exists = timeit.timeit(lambda: boyer_moore_search(text_article2, pattern_exists), number=1000)
time_bm_article2_fake = timeit.timeit(lambda: boyer_moore_search(text_article2, pattern_fake), number=1000)

# Вимірювання часу виконання для алгоритму Кнута-Морріса-Прата
time_kmp_article1_exists = timeit.timeit(lambda: kmp_search(text_article1, pattern_exists), number=1000)
time_kmp_article1_fake = timeit.timeit(lambda: kmp_search(text_article1, pattern_fake), number=1000)

time_kmp_article2_exists = timeit.timeit(lambda: kmp_search(text_article2, pattern_exists), number=1000)
time_kmp_article2_fake = timeit.timeit(lambda: kmp_search(text_article2, pattern_fake), number=1000)

# Вимірювання часу виконання для алгоритму Рабіна-Карпа
time_rk_article1_exists = timeit.timeit(lambda: rabin_karp_search(text_article1, pattern_exists), number=1000)
time_rk_article1_fake = timeit.timeit(lambda: rabin_karp_search(text_article1, pattern_fake), number=1000)

time_rk_article2_exists = timeit.timeit(lambda: rabin_karp_search(text_article2, pattern_exists), number=1000)
time_rk_article2_fake = timeit.timeit(lambda: rabin_karp_search(text_article2, pattern_fake), number=1000)

# Виведення результатів
print("Алгоритм Бойера-Мура:")
print(f"Стаття 1: Час для існуючого підрядка: {time_bm_article1_exists}")
print(f"Стаття 1: Час для вигаданого підрядка: {time_bm_article1_fake}")
print(f"Стаття 2: Час для існуючого підрядка: {time_bm_article2_exists}")
print(f"Стаття 2: Час для вигаданого підрядка: {time_bm_article2_fake}")

print("\nАлгоритм Кнута-Морріса-Прата:")
print(f"Стаття 1: Час для існуючого підрядка: {time_kmp_article1_exists}")
print(f"Стаття 1: Час для вигаданого підрядка: {time_kmp_article1_fake}")
print(f"Стаття 2: Час для існуючого підрядка: {time_kmp_article2_exists}")
print(f"Стаття 2: Час для вигаданого підрядка: {time_kmp_article2_fake}")

print("\nАлгоритм Рабіна-Карпа:")
print(f"Стаття 1: Час для існуючого підрядка: {time_rk_article1_exists}")
print(f"Стаття 1: Час для вигаданого підрядка: {time_rk_article1_fake}")
print(f"Стаття 2: Час для існуючого підрядка: {time_rk_article2_exists}")
print(f"Стаття 2: Час для вигаданого підрядка: {time_rk_article2_fake}")
