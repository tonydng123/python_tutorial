from datetime import datetime
import calendar
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Unpythonic location
    # DAYNAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dayname = Calendar.day_name[datetime.datetime.now().weekday()]
	return f"<p>hello, world! Happy {dayname}</p>"