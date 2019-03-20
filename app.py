from flask import *
import GaugeProjectApache.py.main
import threading
import os
import time
import shutil


class SVGBuildingThread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self):
        """ Method that runs forever """
        GaugeProjectApache.py.main.main()


if os.path.isdir('./static/svg'):
    shutil.rmtree('./static/svg')

os.mkdir('./static/svg')

example = SVGBuildingThread()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dollars')
def dollars():
    return render_template('dollars.html')


@app.route('/kW')
def kW():
    return render_template('kW.html')


@app.route('/kWh')
def kWh():
    return render_template('kWh.html')


@app.route('/kWhHourly')
def hourly():
    return render_template('kWhHourly.html')


if __name__ == '__main__':
    while not os.path.exists(os.path.join('static', 'svg', 'dollars.svg')):
        pass
    app.run()
