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
#              r_id TEXT,
#              u_id INTEGER,
#              location TEXT
#             )''')
# c.execute("DROP TABLE results")
# conn.commit()
# c.execute('''CREATE TABLE wish_list(
#              w_id INTEGER,
#              u_id INTEGER
#             )''')
# c.execute('DROP TABLE result_barcode')
# c.execute('''CREATE TABLE result_barcode(
#              r_id TEXT,
#              barcode TEXT
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

def set_result(message, location):
    import random, string
    u_id = message.from_user.id
    random_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    r_id = str(u_id) + '_' + random_str

    conn = sqlite3.connect(dir_path + '/users.db')
    c = conn.cursor()
    print("BEFOR RESULT INSERT")
    c.execute('''INSERT INTO results VALUES ('%s', %s, '%s')''' % (r_id, u_id, location))
    conn.commit()
    print(u_id)
    c.execute('''SELECT * FROM results''')
    print(c.fetchall())
    # res = c.fetchall()
    return r_id
#
# c.execute("SELECT * FROM results")
# print(c.fetchall())

def associate_brcd_res(r_id, barcode_list):
    conn = sqlite3.connect(dir_path + '/users.db')
    c = conn.cursor()
    for barcode in barcode_list:
        c.execute('''INSERT INTO result_barcode VALUES ('%s', '%s')''' % (r_id, barcode))
        conn.commit()


def get_user_results(u_id):
    conn = sqlite3.connect(dir_path + '/users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM results WHERE u_id=%s''' % u_id)
    res = c.fetchall()
    return res



def barcode_with_result(r_id):
    conn = sqlite3.connect(dir_path + '/users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM result_barcode WHERE r_id='%s' ''' % r_id)
    res = c.fetchall()
    return res
