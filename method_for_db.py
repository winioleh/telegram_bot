import sqlite3, os
from logger import Logger



logger = Logger()
dir_path = os.path.dirname(os.path.realpath(__file__))

conn = sqlite3.connect(dir_path + '/users.db')
c = conn.cursor()
# c.execute('''CREATE TABLE users(
#              u_id INTEGER,
#              chat_id INTEGER,
#              name TEXT
#             )''')
#
# c.execute('''CREATE TABLE results(
#              r_id INTEGER,
#              u_id INTEGER,
#              location TEXT
#             )''')
# c.execute('''CREATE TABLE wish_list(
#              w_id INTEGER,
#              u_id INTEGER
#             )''')
# c.execute('''CREATE TABLE result_barcode(
#              r_id INTEGER,
#              barcode INTEGER
#             )''')
# c.execute('''CREATE TABLE wishlist_barcode(
#              w_id INTEGER,
#              barcode INTEGER
#             )''')


def add_user_to_db(message):

    try:
        u_id = message.from_user.id
        chat_id = message.chat.id
        u_name = message.from_user.first_name + ' ' + message.from_user.last_name

        conn = sqlite3.connect(dir_path + '/users.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users WHERE chat_id=%s''' % chat_id)
        res = c.fetchall()

        if not len(res):
            c.execute('''INSERT INTO users VALUES (%s, '%s', '%s')''' % (u_id,chat_id, u_name))
            conn.commit()
    except  Exception as err:
        logger.write_logs(add_user_to_db.__name__, err)

