from datetime import datetime
import pymysql
import configparser

config = configparser.ConfigParser()
config.read('props.ini')

# Establish connection to DB
conn = pymysql.connect(
    host=config.get('MySQL Creds', 'HOST'),
    port=3306,
    user=config.get('MySQL Creds', 'USER'),
    passwd=config.get('MySQL Creds', 'PASSWORD'),
    db=config.get('MySQL Creds', 'DB'),
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

conn.autocommit(True)
db_name = config.get('MySQL Creds', 'DB_Name')


# Insert data into table
def insert_user(id, name):
    try:
        conn.connect()
        cursor = conn.cursor()

        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f"INSERT into {db_name} VALUES (%s , %s , %s )", (id, name, creation_date))
    # Extra, Handle if ID exists
    except pymysql.err.IntegrityError:

        new_id = get_ids() + 1

        conn.connect()
        cursor = conn.cursor()

        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f"INSERT into {db_name} VALUES (%s , %s , %s )", (new_id, name, creation_date))
        print(f"ID was in use, inserted as {new_id} instead")
    finally:
        cursor.close()
        conn.close()


# Updating data inside the table
def update_user(name, id):
    try:
        conn.connect()
        cursor = conn.cursor()

        cursor.execute(f"UPDATE {db_name} SET name = %s WHERE id =  %s", (name, id))
    except:
        print("Error")
    finally:
        cursor.close()
        conn.close()


# Delete user from table
def delete_user(id):
    try:
        conn.connect()
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {db_name} WHERE id = %s", id)
    except:
        print("Error")
    finally:
        cursor.close()
        conn.close()


# get user by user id
def get_id(id):
    try:
        conn.connect()
        cursor = conn.cursor()

        name = ''
        cursor.execute(f"SELECT * FROM {db_name} WHERE id = %s", id)
        for row in cursor:
            name = row['name']
        return name
    except:
        print("Error")
    finally:
        cursor.close()
        conn.close()


def get_table():
    try:
        conn.connect()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {db_name}")
        for row in cursor:
            print(row)
    except:
        print("Error")
    finally:
        cursor.close()
        conn.close()


def get_ids():
    try:
        conn.connect()
        cursor = conn.cursor()

        cursor.execute(f"SELECT max(id) FROM {db_name}")
        ids = cursor.fetchall()
        return ids[0]['max(id)']
    except:
        print("Error")
    finally:
        cursor.close()
        conn.close()

