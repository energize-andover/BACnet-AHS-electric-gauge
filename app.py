import os
import shutil
import threading

from flask import *

import GaugeProjectApache.py.main


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

gauge_base_path = os.path.join(os.sep, 'static', 'svg')


@app.route('/')
def index():
    return redirect("/kW")


@app.route('/dollars')
def dollars():
    return render_template('gaugePage.html', title="Cost | Electricity Statistics Dashboard",
                           gauge_path=os.path.join(gauge_base_path, 'dollars.svg'))


@app.route('/kW')
def kW():
    return render_template('gaugePage.html', title="Kilowatts | Electricity Statistics Dashboard",
                           gauge_path=os.path.join(gauge_base_path, 'kw.svg'))


@app.route('/kWh')
def kWh():
    return render_template('gaugePage.html', title="Kilowatt-Hours | Electricity Statistics Dashboard",
                           gauge_path=os.path.join(gauge_base_path, 'kwh.svg'))


@app.route('/kWhHourly')
def hourly():
    return render_template('gaugePage.html', title="Kilowatt-Hours | Electricity Statistics Dashboard",
                           gauge_path=os.path.join(gauge_base_path, 'kWhHourly.svg'))


if __name__ == '__main__':
    while not os.path.exists(os.path.join('static', 'svg', 'dollars.svg')):
        pass
    app.run()
