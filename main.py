# Написать программу по подсчёту символов в строке.
# Нельзя учитывать пробелы и знаки пунктуации

sentence = input()
count_symb = 0
for i in sentence:
    if i not in '-, !,  , . , , ,,?, :, ;':
        count_symb += 1

print(count_symb)

