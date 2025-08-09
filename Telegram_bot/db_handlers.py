import random
from connections import conn
from psycopg2.extras import DictCursor
import message_handlers

def choose_random():
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT * FROM words ORDER BY random() LIMIT 1;")
    random_word = cursor.fetchone()
    return random_word['word_eng'], random_word['word_rus']

def choose_random_only_rus():
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT * FROM words ORDER BY random() LIMIT 1;")
    random_word = cursor.fetchone()
    return random_word['word_rus']


