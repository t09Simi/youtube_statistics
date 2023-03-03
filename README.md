# YouTube Video Statistics Application using Flask
This application shows trending videos in youtube based on the views, likes, comments, dislikes on the videos and the date it was published. The application is made using Flask, SQLite3 and deployed using Render.  

Create a folder named 'youtube_statistics' and place all your files here. The dataset used for making this application can be found here https://www.kaggle.com/datasets/datasnaek/youtube-new?select=GBvideos.csv. This csv file will be used to create database for our application 'youtube_data.db'. The csv file is placed in the folder 'data_of_gb_videos_category'.

##### Linking Tables

We will create two related tables from the 'GBvideos.csv' file. For the first table we will create a primary key called 'id' that is auto-incremented to uniquely identify the videos. For the second table 'details_id' is a foreign key which references the 'id' of the first table, creating a relationship between them.

##### Csv file parsing and adding it to database

The 'parse_csv.py' file will read and parse the csv file. We will provide a loop to read each rows and print them into the screen. In the same file we create the two tables and insert data into them. First run cd youtube_statistics and execute this command this will help create the database.
   
        youtube_statistics/python3 parse_csv.py

Now we will download flask and setup virtual environment for our application using these commands:
                        
        pyenv install 3.7.0         # this installs 3.7.0 in the environment to use
        pyenv local 3.7.0           # this sets the local version of python to 3.7.0
        python3 -m venv .venv       # creates the virtual environment
        source .venv/bin/activate   # this activates the virtual environment
        pip install --upgrade pip   # this installs pip and upgrades it if its required
        pip install flask           # this installs flask to build application

##### Creating web pages

We will create a templates folder and keep all our html pages in that file. The 'index.html' file is the first file that you will see when running the application. The 'index.html' file has link to the 'videos.html' and 'likes.html' files. 

In 'videos.html' you will see the list of Top 50 trending videos based on the views and by clicking each of their IDs you will see the statistics associated with that video such as likes, dislikes, comments and date published which is from  the 'statistics.html' file.

The logic of the application is written in 'video_statistics.py' file. This file will render the html page using the @route method and execute the sql command for that web page.

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

##### Using Render for deployment 

         






