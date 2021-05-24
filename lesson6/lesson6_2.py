def print_surname_name(surname, name):
    print(f"Ваше имя {surname}")
    print(f"Ваша фамилия {name}")


    def print_name_list(names_list):
        for i in names_list:
            print()
            print_surname_name(i[0], i[1])


    print_name_list([["Тилек","Байтаев"]])