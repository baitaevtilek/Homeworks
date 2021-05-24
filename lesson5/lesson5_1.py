todos = []

while True:
    action = input("Выберите действие: Y) Добавить задачу V) Позакать задачи C) Отметить как выполненное")
    if action == "Y":
        todo = input("Задача: ")
        deadline = input("Дэдлайн: ")
        date_added = input("Добавленно: ")
        completed = False
        todos.append([todo, deadline, date_added, completed])
        print("Задача добавленна!")
    elif action == "V":
        print()
        if len(todos) == 0:
            print("Нет Задач!")
        print('Задача      Дэдлайн     Дата добавления    Выполненно')
        for pos, i in enumerate(todos):
            print(pos, i[0], i[1], i[2], i[3])
        print()
    elif action == "C":
        index = int(input("Выберите задачу что бы отметить "))
        todos[index][3] = True
        print(todos)
    else:
        print("Выберите правильный вариант!\n"
              