from recipeapi import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# how to use migrations
# in windows, in terminal: set FLASK_APP=run.py
# flask db init
# flask db migrate
# flask db upgrade
# might need to import citext folder inside versions py module

# how to create tables with create_all from terminal https://stackoverflow.com/q/58536224/7858114