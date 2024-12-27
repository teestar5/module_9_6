# def all_variants(text):
#     """
#     Генератор, который возвращает все подпоследовательности строки text.
#
#     :param text: Исходная строка, из которой будут извлекаться подпоследовательности.
#     """
#     n = len(text)  # Получаем длину строки
#     # Внешний цикл по начальному индексу подпоследовательности
#     for start in range(n):
#         # Внутренний цикл по конечному индексу подпоследовательности
#         for end in range(start + 1, n + 1):
#             yield text[start:end]  # Генерируем и возвращаем подпоследовательность
#
#
# # Пример использования функции-генератора
# a = all_variants("abc")  # Создаем генератор для строки "abc"

# for i in a:
#     print(i)  # Выводим каждую подпоследовательность

def all_variants(text):
    x = 0
    y = 0
    for x in range(len(text)):
        for y in range(x + 1, len(text) + 1):
            yield text[x:y]


a = all_variants("abc")
for i in a:
    print(i)