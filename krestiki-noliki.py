table=[['-']*3 for _ in range(3)]
    
def open_table(f):
    print('  0 1 2')
    for i in range(len(table)):
        print(str(i)+' '+' '.join(table[i]))

def player_input(t):
    while True:
        coordin=input('Введите координаты:').split()
        if len(coordin) != 2:
            print('Введите две координаты')
            continue
        if not(coordin[0].isdigit() and coordin[1].isdigit()):
            print('Введите числа')
            continue
        x,y=map(int, coordin)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вышли из диапазона')
            continue
        if t[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

def winner(t,user):
    win_var=[]
    for n in t:
        win_var+= n
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indexi = set([i for i, x in enumerate(win_var) if x == user])
    for p in positions:
        if len(indexi.intersection(set(p)))==3:
            return True
    return False

count = 0
while True:
    if count%2==0:
        user='x'
    else:
        user='0'
    open_table(table)
    if count<9:
        x,y = player_input(table)
        table[x][y] = user
    if count == 9:
        print('Ничья')
        break
    if winner(table, user):
        open_table(table)
        print(f'Выиграл {user}')
        break
    count+=1