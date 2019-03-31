import os
import shutil
import threading

from flask import *

import GaugeProjectApache.py.main

HOST_PREFIX = ""
app = Flask(__name__)


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


def main():
    if os.path.isdir('./static/svg'):
        shutil.rmtree('./static/svg')

    os.mkdir('./static/svg')

    example = SVGBuildingThread()

    gauge_base_path = os.path.join(os.sep, 'static', 'svg')

    @app.route(HOST_PREFIX + '/')
    def index():
        return redirect(HOST_PREFIX + "/kW")

    #Add headers to both force latest IE rendering engine or Chrome Frame,
    #and also to cache the rendered page for 10 minutes.

    @app.after_request
    def add_header(r):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    @app.route(HOST_PREFIX + '/dollars')
    def dollars():
        return render_template('gaugePage.html', title="Cost (Reset Daily) | Electricity Statistics Dashboard",
                               gauge_path=os.path.join(gauge_base_path, 'dollars.svg'))

    @app.route(HOST_PREFIX + '/documentation')
    def documentation():
        return render_template('documentation.html')

    @app.route(HOST_PREFIX + '/kW')
    def kW():
        return render_template('gaugePage.html', title="Kilowatts (Live) | Electricity Statistics Dashboard",
                               gauge_path=os.path.join(gauge_base_path, 'kw.svg'))

    @app.route(HOST_PREFIX + '/kWh')
    def kWh():
        return render_template('gaugePage.html',
                               title="Kilowatt-Hours (Reset Daily) | Electricity Statistics Dashboard",
                               gauge_path=os.path.join(gauge_base_path, 'kwh.svg'))

    @app.route(HOST_PREFIX + '/kWhHourly')
    def hourly():
        return render_template('gaugePage.html', title="Kilowatt-Hours (Hourly) | Electricity Statistics Dashboard",
                               gauge_path=os.path.join(gauge_base_path, 'kWhHourly.svg'))

    app.jinja_env.globals['host_prefix'] = HOST_PREFIX
    app.static_url_path = '{0}/static'.format(HOST_PREFIX)

    # remove old static map
    url_map = app.url_map
    try:
        for rule in url_map.iter_rules('static'):
            url_map._rules.remove(rule)
    except ValueError:
        # no static view was created yet
        pass

    # register new; the same view function is used
    app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file)

    while not os.path.exists(os.path.join('static', 'svg', 'dollars.svg')):
        pass


main()

if __name__ == '__main__':
    app.run()
