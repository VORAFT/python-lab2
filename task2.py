def insert_after_element(lst, target, new_element):

    if target in lst:
        index = lst.index(target)
        lst.insert(index + 1, new_element)
        print(f"Елемент '{new_element}' успішно додано після '{target}'.")
    else:
        print(f"Помилка! Елемента '{target}' немає у введеному списку.")
    
    print("Результатуючий список:", lst)


user_input = input("Введіть елементи списку через пробіл: ")
my_list = user_input.split()

target_elem = input("Введіть елемент, ПІСЛЯ якого потрібно зробити вставку: ")
new_elem = input("Введіть новий елемент, який треба вставити: ")

insert_after_element(my_list, target_elem, new_elem)