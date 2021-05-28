# Homeworks
Hw6


print("*" * 1, " Игра Крестики-нолики на двоих ", "*" * 1)
print("Удачной иргы))")
plane = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"],
]

def check_winer(p):
    win = True
    for i in range(3):
        row = plane[i]
        start = ""
        for k in row:
            if k == "*":
                win = False
                break
            if not start:
                start = k
            else:
                if start == k:
                    start = k
                else:
                    win = False
                    break
                if win:
                    return start

    if p[0][0] == p[0][1] == p[0][2]:
        return  p[0][0]
    if p[0][0] == p[1][1] == p[2][2]:
        return p[0][0]
    if p[0][2] == p[1][1] == p[2][0]:
        return p[2][0]

    if p[1][0] == p[1][1] == p[2][2]:
        return p[1][0]
    if p[2][0] == p[2][1] == p[2][2]:
        return p[2][2]


def input_x_y():
    return int(input()) - 1, int(input()) - 1


def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print("-"*9)

def main():
    print_plane(plane)
    player_1_x, player_1_y = input_x_y()
    plane[player_1_x][player_1_y] = "x"
    print_plane(plane)
    player_2_x, player_2_y = input_x_y()
    plane[player_2_x][player_2_y] = "0"
    print_plane(plane)


while True:
    main() 
