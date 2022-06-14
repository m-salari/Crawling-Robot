from random import choice


def send_personally_message(app, texts_list):
    try:
        with open(f'./telegram_username.txt', 'r') as f:
            users_list = f.readlines()

        for user in users_list:
            if not '-' == user[0]:
                app.send_message(user, choice(texts_list))
                users_list[users_list.index(user)] = f"-{users_list[users_list.index(user)]}"
                with open(f'./telegram_username.txt', 'w') as f:
                    for i in users_list:
                        f.write(i)
        print('Done send.\n')
        return users_list

    except FileNotFoundError:
        raise FileNotFoundError('this file is not TEXT file. please first get ids and write to TEXT file.')
