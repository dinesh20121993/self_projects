import psycopg2
from random_user_generator import generate_usr
con = psycopg2.connect(
                    host = "localhost", 
                    port = "5432", 
                    database = "dinesh", 
                    user = "postgres",
                    password = "postgres"
                    )
cursor = con.cursor()
def connect_to_db():
    try:
        print("\nConnecting to Database .......")
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()[0]
        print("\nconnected succesfully......")
        print("\nversion : ",db_version)
        cursor.close()
    except(Exception , psycopg2.DatabaseError) as e:
        print(e)
    finally:
        con.close()

def create_table():

    try:
        cursor = con.cursor()
        create_table_command = """

        CREATE TABLE IF NOT EXISTS public.random_data
        (
            "ID" SERIAL PRIMARY KEY,
            "Name" VARCHAR NOT NULL,
            "Email" VARCHAR NOT NULL,
            "Age" integer NOT NULL,
            "Gender" VARCHAR NOT NULL,
            "User_name" VARCHAR NOT NULL,
            "Password" VARCHAR NOT NULL,
            "Address" VARCHAR NOT NULL
        )
        TABLESPACE pg_default;

        """
        cursor.execute(create_table_command)
        con.commit()
        print("Table Created")
        cursor.close()
    except(Exception , psycopg2.DatabaseError) as e:
        print(e)
    finally:
        con.close()


def insert_data(data):
    try:
        command = """
        INSERT INTO public.random_data
        (
           "Name","Email","Age","Gender","User_name","Password","Address"
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(command,(data["name"],data["e-mail"],data["age"],data["gender"],data["user_name"],data["password"],data["address"]))
        con.commit()
    except(Exception , psycopg2.DatabaseError) as e:
        print(e)


def get_user_data():
    cursor.execute('SELECT "ID", "Name", "Email", "Age", "Gender", "User_name", "Password", "Address"FROM public.random_data;')
    results = cursor.fetchmany(200)
    return results


def populate(num):
    print(f"Populating {num} new users into table....")
    i = 0
    while i < num:
        data = generate_usr()
        insert_data(data)
        i = i+1
    print(f"succesfully inserted {num} users.")



