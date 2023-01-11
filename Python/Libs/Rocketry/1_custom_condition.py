from rocketry import Rocketry
from rocketry.conds import daily, time_of_week
from pathlib import Path

app = Rocketry()

@app.cond()
def file_exists(file):
    return Path(file).exists()

@app.task(daily.after("08:00") & file_exists("start.py"))
def do_work():
    print('Doing work')

app.run()