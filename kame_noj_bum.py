player1 = 0
computer1 = 0
while True:
    from random import choice
    commands = ['Камень','Ножница','Бумага']
    computer = choice(commands)
    player = input("выберите один из этих ('Камень','Ножница','Бумага')")
    if player == "Камень":
        if computer == commands[1]:
            player1+=1
            print(f"Вы победили!!!\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
        elif computer == commands[2]:
            computer1+=1
            print(f"Вы проиграли(((\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
    elif player=="Ножница":
        if computer == commands[0]:
            computer1+=1
            print(f"Вы проиграли(((\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
        elif computer == commands[2]:
            player1+=1
            print(f"Вы победили!!!\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
    elif player=="Бумага":
        if computer == commands[0]:
            player1+=1
            print(f"Вы победили!!!\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
        elif computer == commands[1]:
            computer1+=1
            print(f"Вы проиграли(((\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
    elif player==computer:
        print(f"Ничья\nваш счет{player1}\nкомпьютер{computer1}")
    else:
        print("выберите один из этих ('Камень','Ножница','Бумага')")
    if computer1>5 :
        print(f"Вы проиграли(( ваш счет{player1}\nкомпьютер :{computer1}\nДосвидание")
        break
    elif player1>5:
        print(f"Вы победили!!\nваш счет{player1}\nкомпьютер{computer1}")
        break


    # Компьютер выбрал {computer}. 
# ваш счет{player1}\n,компьютер{computer1}
# (f"Вы победили!!!\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")
# (f"Вы проиграли(((\nКомпьютер выбрал : {computer}.\nВаш счет : {player1}\nКомпьютер : {computer1}")