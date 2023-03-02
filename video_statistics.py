import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

database_name = 'youtube_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videos')
def videos():
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from details ORDER BY views DESC LIMIT 50")
    row_videoinfo = cur.fetchall()
    conn.close()
    return render_template('videos.html',row_videoinfo=row_videoinfo)

@app.route('/statistics/<id>')
def statistics(id):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from statistics where id =?",([id]))
    row_stats = cur.fetchall()
    conn.close()
    return render_template('statistics.html',row_stats=row_stats)

@app.route('/likes')
def likes():
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    query = """
    SELECT details.title, details.views, statistics.likes
    FROM details
    JOIN statistics ON details.id = statistics.details_id
    ORDER BY statistics.likes DESC LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(query)
    likes = cur.fetchall()
    conn.close()
    return render_template('likes.html',likes=likes)