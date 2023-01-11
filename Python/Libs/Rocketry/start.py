from rocketry import Rocketry
from rocketry.conds import secondly

app = Rocketry()

@app.task(secondly)
def do_daily():
    print('Doing daily task')

if __name__ == '__main__':
    app.run()
