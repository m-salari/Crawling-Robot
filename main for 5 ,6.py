from pyrogram import Client
from five import *
from six import *


api_id = 19107939
api_hash = '3cdf230306c2acf1e8aaf7dfb0ad6392'

app = Client('root', api_id=api_id, api_hash=api_hash)
app.start()

if __name__ == '__main__':

    print("""
    1 --> enter group id and creates a text file where there are IDs.
    2 --> Enter your text to send to all and then the app will do it.
    end --> exit
    """)

    while 1:
        text_list_for_send = []
        get_command = input('enter your command: ')
        if get_command == "1":
            group_id = input('enter group id: ')
            found_chat_id(app, group_id)

        elif get_command == "2":
            while 2:
                text_for_send = input('enter text for send to all members: ')
                if text_for_send in ['end', 'END', 'e', 'E']:
                    break
                text_list_for_send.append(text_for_send)
            
            edited = send_personally_message(app, text_list_for_send)

        elif get_command in ['end', 'END', 'e', 'E']:
            print('\n..:: EXIT ::..')
            break

        else:
            print('your command is invalid.')
