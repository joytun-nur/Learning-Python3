#------------------------------------
#    Working with database : SQlite
#    Joytun Nur Sultana :
#------------------------------------

from Database import MyDatabase


# Program entry point
def main():
    dbms = MyDatabase.MyDatabase(MyDatabase.SQLITE, dbname='mydb.sqlite')

    # Create Tables
    # dbms.create_db_tables()

    # # dbms.insert_single_data()

    # dbms.print_all_data(MyDatabase.USERS)
    # dbms.print_all_data(MyDatabase.ADDRESSES)

    dbms.sample_query()   # simple query
    dbms.sample_delete()  # delete data
    dbms.sample_insert()  # insert data
    dbms.sample_update()  # update data


# run the program
if __name__ == "__main__": main()
