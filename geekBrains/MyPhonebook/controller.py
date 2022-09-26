import user_input
import funcs

def click():
    path = 'geekBrains/MyPhonebook/data.csv'
    while True:
        try:
            user_choice = int(user_input.menu())
        except:
            user_input.error()
            continue
        if user_choice == 1:
            funcs.add_info(path)
            break
        elif user_choice == 2:
            funcs.find_num(path)
            break
        elif user_choice == 3:
            funcs.delete_item(path)
            break
        elif user_choice == 4:
            funcs.show_all(path)
            break
        elif user_choice == 5:
            funcs.change_item(path)
            break
        else:
            user_input.error()

    



