import sqlite3

class ChatGPTDatabase:
     def __init__(self, db_name):
          self.db_name = db_name
          self.conn = sqlite3.connect(db_name)
          self.cursor = self.conn.cursor()

     def create_table(self, table_name, columns):
               """
               Create a new table in the database with the given name and column.
               The columns parameter should be comma-seperated string of columns.
               """
               create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
               self.cursor.execute(create_table_sql)
               self.conn.commit()

     def insert_record(self, table_name, columns, record):
        '''
        Insert a record to a target table with values separate by a comma.
        ''' 
        sql = f'INSERT INTO {table_name}({columns}) VALUES ({record})'
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

     def retrieve_records(self, table_name, conditions=None):
        """
        Retrieves all records from the specified table in the database.
        The conditions parameter should be a string that represents a SQL WHERE clause.
        """
        select_sql = f"SELECT * FROM{table_name}"
        if conditions:
                select_sql += f" WHERE {conditions}"
        self.cursor.execute(select_sql)
        return self.cursor.fetchall()
     
     def close(self):
        print('db closed')
        self.cursor.close()
        self.conn.close()