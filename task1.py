sentence = input("Введіть речення (щонайменше 7 слів): ")
words = sentence.split()

while len(words) < 7:
    print("Помилка! У реченні менше 7 слів.")
    sentence = input("Введіть речення ще раз: ")
    words = sentence.split()

words[0], words[-1] = words[-1], words[0]

result_sentence = " ".join(words)

print("Результат:")
print(result_sentence)