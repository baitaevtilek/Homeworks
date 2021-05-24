# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return
#
#
# print(sum(2, 63, 3, 6))



# def ab(**Kwargs):
#     return kwargs
#
#
# print(sum(a=2, c=3, d=2, e=2))

def print_name_surname(name, surname, **kwargs):
    if 'itchestvo' in kwargs:
        return f"{name} {surname} {kwargs['otchestvo']}"
    return f"{name} {surname}"




name = "Tilek"
surname = "baitaev"
otchestvo = input()
print(print_name_surname(name, surname, 18, 2002))