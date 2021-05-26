# Написать программу по подсчёту слов в тексте.
# Текст ввести в консоли.
# Далее вывести сколько раз какое слово повторяется в тексте.

text_str = input()
text_split = text_str.split()

d = {}

for word in text_split:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)



