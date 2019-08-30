import mysql.connector
from mysql.connector import Error
from datetime import datetime
import logging


g_dbconfig = {
  'user': 'root',
  'password': 'root@MYSQL',
  'host': '127.0.0.1',
  'database': 'sakila',
  'raise_on_warnings': True
}


logging.basicConfig(filename='MySQLDB.log', filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s- %(process)d: %(message)s')


def stamper(fmt='%Y-%m-%d %H:%M:%S'):
    while True:
        yield datetime.strftime(datetime.now(), fmt)


def logger(*arg, **kwargs):
    logging.debug(*arg, **kwargs)


class MySQLDB(object):
    """
    MySQL Connector/Python Wrapper
    """
    _connection = None
    _instance = None
    _config = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            logger(f"new obj: {cls._instance}")
        return cls._instance

    def __init__(self, *args, **kwargs):
        g_dbconfig.update(kwargs)
        self._config = g_dbconfig
        logger(f"init with: {self._config}")

    def __enter__(self):
        logger(f"__enter__:")
        if self._connection is None:
            try:
                self._connection = mysql.connector.connect(**self._config)

                if self._connection.is_connected():
                    server_info = self._connection.get_server_info()
                    logger(f"Connected to MySQL database, version: {server_info}")

                    cursor = self._connection.cursor()
                    cursor.execute("select database();")
                    db_info = cursor.fetchone()
                    logger(f"You connected to DB: {db_info}  ")

            except Error as err:
                logging.critical("Error while connecting to MySQL: ", err)
                logging.critical("exited......")
        logger(f"enter end...")
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger(f"__exit__:")
        if self._connection.is_connected():
            self._connection.cursor().close()
            self._connection.close()
            self._connection = None
            logger("MySQL connection is closed")
        logger(f"exit end...")


if __name__ == '__main__':
    with MySQLDB() as db:
        logger('in db')
        cursor = db.cursor()
        cursor.execute("SHOW TABLES;")
        for table in cursor:
            print(table)

    logger("-"*40)

    with MySQLDB(database='world') as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name, CountryCode, Population FROM city;")
        for row in cursor:
            print(row)

