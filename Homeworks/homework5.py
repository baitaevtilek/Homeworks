
d_en = {
    "cow": "корова",
    "human": "человек",
    "tree": "дерево",
    "cheir": "стул",
    "snow": "снег",
}
d_rus = {
    "корова": "cow",
    "человек": "human",
    "дерево": "tree",
    "стул": "chair",
    "снег": "snow",

}
d_kgrus = {
    "уй": "корова",
    "адам": "человек",
    "дарак": "дерево",
    "отургуч": "стул",
    "кар": "снег"
}
d_kgen = {
    "cow": "уй",
    "human": "адам",
    "tree": "дарак",
    "chair": "отургуч",
    "snow": "кар"
}
while True:
    alldict =["Язык оригинлала Англ",d_en,"Язык перевода Русский"],\
             ["Язык оригинала Русс",d_rus,"Язык перевода English"],\
             ["Язык оригинала Русс",d_kgrus,"Язык перевода Кыргызский"],\
             ["Язык оригинала Англ",d_kgen,"Язык перевода Кыргызский"]
   try:
    translateword=input("Введите слово>>")
    for dict in alldict :
         for key in dict[1]:
            if key==translateword:
                print(dict[0])
                print(dict[2])
                print(dict[1][key])

