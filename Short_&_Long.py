# Найти самое короткое и самое длинное слово в строке

s = input()
s = s.split()
print(max(s, key=len))
print(min(s, key=len))