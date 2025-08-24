# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

from mysql import connector
from quotes_project.items import QuotesProjectItem
import re

class QuotesProjectPipeline:
    """ Save records pulled from webpage to MySQl Scraping database"""
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect_to_db()
        self.create_table()
        #self.process_quote()

    def connect_to_db(self):
        """ COnnect to database """
        try:
            self.conn = connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'MySQL%958#treebeard',
                database = 'scraping'

            )
            self.cursor = self.conn.cursor()
            print("Connection succeeded")
        except connector.Error as err:
            print(f"Error connecting to MySQL: {err}")

    def create_table(self):
        """ Create table if it does not exist """
        if self.cursor:
            table_create_query = """
            CREATE TABLE IF NOT EXISTS quotes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                author VARCHAR(255),
                text VARCHAR(255));
            """
            
            try:
                self.cursor.execute(table_create_query)
                self.conn.commit()
                print("Table created")
            except connector.Error as err:
                print(f"Error creating table: {err}")

    def process_item(self, item, spider): # must be called process_item to be called
        """ Insert scraped data into quotes table"""
        print("The process_quote function is running")
        insert_query = """ INSERT INTO quotes (author, text) VALUES (%s, %s);
                       """
        try:
            self.cursor.execute(insert_query, (item['author'][0],item['text'][0].replace("\u201c", "").replace("\u201d", "")))
            self.conn.commit()
            print(f"Record loaded and saved: {item['author'][0]} and {item['text'][0].replace("\u201c", "").replace("\u201d", "")}")
        except connector.Error as err:
            print(f"Error saving data to table: {err}")

    def close_spider(self, spider):
        """ Close cursor and database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
