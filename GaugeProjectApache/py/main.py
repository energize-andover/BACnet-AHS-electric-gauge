import pygal
import pandas as pd
import time
from GaugeProjectApache.py.building_data_requests import get_value
import numbers
from datetime import timedelta
import datetime
import os


def interpret_csv(facility):
    try:
        # Read spreadsheet into a dataframe.
        # Each row contains the following:
        #   - Label
        #   - Facility
        #   - Instance ID of electric meter
        df = pd.read_csv(os.path.join('GaugeProjectApache', 'csv', 'ahs_power.csv'))

        # Output column headings
        # print('Feeder,Meter,Units')

        # Iterate over the rows of the dataframe, getting meter readings for each feeder
        # Iterate over the rows of the dataframe, getting meter readings for each feeder
        for index, row in df.iterrows():
            # Retrieve data
            value, units = get_value(row['Facility'], row['Meter'])

            # Prepare to print
            value = int(value) if isinstance(value, numbers.Number) else ''

            # Output CSV format
            if facility == row['Label']:
                return (value)
                # print(facility + value)
                # print(test)

    except KeyboardInterrupt:
        print('Bye')
        import sys
        sys.exit()


def main():
    gauge_chart = pygal.Gauge(human_readable=True)

    main_kwh_constant = interpret_csv("Main (kWh)")
    while main_kwh_constant == '' or main_kwh_constant is None:
        main_kwh_constant = 0
    main_kwh_constant = int(main_kwh_constant)

    gym_kwh_constant = interpret_csv("DG (kWh)")
    while gym_kwh_constant == '' or gym_kwh_constant is None:
        gym_kwh_constant = 0
    gym_kwh_constant = int(gym_kwh_constant)

    kitchen_kwh_constant = interpret_csv("DE (kWh)")
    while kitchen_kwh_constant == '' or kitchen_kwh_constant is None:
        kitchen_kwh_constant = 0
    kitchen_kwh_constant = int(kitchen_kwh_constant)

    collins_center_kwh_constant = interpret_csv("AMDP (kWh)")
    while collins_center_kwh_constant == '' or collins_center_kwh_constant is None:
        collins_center_kwh_constant = 0
    collins_center_kwh_constant = int(collins_center_kwh_constant)

    six = False
    seven = False
    eight = False
    nine = False
    ten = False
    eleven = False
    twelve = False
    one = False
    two = False
    three = False
    gauge_chart.title = 'Electricity used hourly in kWh all of ahs'
    gauge_chart.range = [0, 7000]
    try:

        percent_formatter = lambda x: '{:.10g}%'.format(x)
        dollar_formatter = lambda x: '{:.10g}$'.format(x)
        kW_formatter = lambda x: '{:.10g}kW'.format(x)
        kWh_formatter = lambda x: '{:.10g}kWh'.format(x)
        while True:

            currentDT = datetime.datetime.now()
            currentDT2 = datetime.date.today()

            main_kw = interpret_csv("Main (kW)")
            if main_kw == '' or main_kw is None:
                main_kw = 0
            main_kw = int(main_kw)

            main_kwh = interpret_csv("Main (kWh)")
            if main_kwh == '' or main_kwh is None:
                main_kwh = 0
            main_kwh = int(main_kwh)
            main_kwh = main_kwh - main_kwh_constant

            gym_kw = interpret_csv("DG (kW)")
            if gym_kw == '' or gym_kw is None:
                gym_kw = 0
            gym_kw = int(gym_kw)

            gym_kwh = interpret_csv("DG (kWh)")
            if gym_kwh == '' or gym_kwh is None:
                gym_kwh = 0
            gym_kwh = int(gym_kwh)
            gym_kwh = gym_kwh - gym_kwh_constant

            kitchen_kw = interpret_csv("DE (kW)")
            if kitchen_kw == '' or kitchen_kw is None:
                kitchen_kw = 0
            kitchen_kw = int(kitchen_kw)

            kitchen_kwh = interpret_csv("DE (kWh)")
            if kitchen_kwh == '' or kitchen_kwh is None:
                kitchen_kwh = 0
            kitchen_kwh = int(kitchen_kwh)
            kitchen_kwh = kitchen_kwh - kitchen_kwh_constant

            collins_center_kw = interpret_csv("AMDP (kW)")
            if collins_center_kw == '' or collins_center_kw is None:
                collins_center_kw = 0
            collins_center_kw = int(collins_center_kw)

            collins_center_kwh = interpret_csv("AMDP (kWh)")
            if collins_center_kwh == '' or collins_center_kwh is None:
                collins_center_kwh = 0
            collins_center_kwh = int(collins_center_kwh)
            collins_center_kwh = collins_center_kwh - collins_center_kwh

            kW = pygal.SolidGauge(
                half_pie=True, inner_radius=0.70,
                style=pygal.style.styles['default'](value_font_size=10))
            kW.add('AHS MAIN aka all of AHS', [{'value': main_kw, 'max_value': 750}],
                   formatter=kW_formatter)
            kW.add('AHS GYM', [{'value': gym_kw, 'max_value': 200}],
                   formatter=kW_formatter)
            kW.add('AHS COLLINS CENTER', [{'value': collins_center_kw, 'max_value': 250}],
                   formatter=kW_formatter)
            kW.add('AHS KITCHEN', [{'value': kitchen_kw, 'max_value': 150}],
                   formatter=kW_formatter)
            kW.render_to_file("static/svg/kw.svg")

            kWh = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
                                   style=pygal.style.styles['default'](value_font_size=10))
            kWh.add('AHS MAIN aka all of AHS', [{'value': main_kwh, 'max_value': 50}],
                    formatter=kWh_formatter)
            kWh.add('AHS GYM', [{'value': gym_kwh, 'max_value': 20}],
                    formatter=kWh_formatter)
            kWh.add('AHS COLLINS CENTER', [{'value': collins_center_kwh, 'max_value': 20}],
                    formatter=kWh_formatter)
            kWh.add('AHS KITCHEN', [{'value': kitchen_kwh, 'max_value': 20}],
                    formatter=kWh_formatter)
            kWh.render_to_file("static/svg/kwh.svg")

            dollar = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
                                      style=pygal.style.styles['default'](value_font_size=10))
            dollar.add('AHS MAIN aka all of AHS', [{'value': int(main_kwh * 0.12), 'max_value': int(0.12 * 50)}],
                       formatter=dollar_formatter)
            dollar.add('AHS GYM', [{'value': int(gym_kwh * 0.12), 'max_value': int(0.12 * 20)}],
                       formatter=dollar_formatter)
            dollar.add('AHS COLLINS CENTER', [{'value': int(0.12 * collins_center_kwh), 'max_value': int(0.12 * 20)}],
                       formatter=dollar_formatter)
            dollar.add('AHS KITCHEN', [{'value': int(0.12 * kitchen_kwh), 'max_value': int(0.12 * 20)}],
                       formatter=dollar_formatter)
            dollar.render_to_file("static/svg/dollars.svg")
            if currentDT.hour == 23:
                current_day = currentDT2.day + timedelta(days=1)
            try:
                current_day
            except NameError:
                print("kWh hourly not ready yet")
            else:
                if currentDT2.day == current_day:
                    if 5 <= currentDT.hour < 16:
                        global six_am_kwh, seven_am_kwh, eight_am_kwh, nine_am_kwh, ten_am_kwh, eleven_am_kwh, twelve_pm_kwh, one_pm_kwh, two_pm_kwh, three_pm_kwh
                        if (int(currentDT.hour) == 6) and not six:
                            six = True
                            gauge_chart.add('6 am', 0)
                            six_am_kwh = interpret_csv("Main (kWh)")
                            if six_am_kwh == '' or six_am_kwh is None:
                                six_am_kwh = interpret_csv("Main (kWh)")
                            six_am_kwh = int(six_am_kwh)

                        if (int(currentDT.hour) == 7) and (seven == False):
                            seven = True
                            seven_am_kwh = interpret_csv("Main (kWh)")
                            if seven_am_kwh == '' or seven_am_kwh is None:
                                seven_am_kwh = interpret_csv("Main (kWh)")
                            seven_am_kwh = int(seven_am_kwh)
                            gauge_chart.add('7 am', seven_am_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 8) and (eight == False):
                            eight = True
                            eight_am_kwh = interpret_csv("Main (kWh)")
                            if eight_am_kwh == '' or eight_am_kwh is None:
                                eight_am_kwh = interpret_csv("Main (kWh)")
                            eight_am_kwh = int(eight_am_kwh)
                            gauge_chart.add('8 am', eight_am_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 9) and (nine == False):
                            nine = True
                            nine_am_kwh = interpret_csv("Main (kWh)")
                            if nine_am_kwh == '' or nine_am_kwh is None:
                                nine_am_kwh = interpret_csv("Main (kWh)")
                            nine_am_kwh = int(nine_am_kwh)
                            gauge_chart.add('9 am', nine_am_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 10) and (ten == False):
                            ten = True
                            ten_am_kwh = interpret_csv("Main (kWh)")
                            if ten_am_kwh == '' or ten_am_kwh is None:
                                ten_am_kwh = interpret_csv("Main (kWh)")
                            ten_am_kwh = int(ten_am_kwh)
                            gauge_chart.add('10 am', ten_am_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 11) and (eleven == False):
                            eleven = True
                            eleven_am_kwh = interpret_csv("Main (kWh)")
                            if eleven_am_kwh == '' or eleven_am_kwh is None:
                                eleven_am_kwh = interpret_csv("Main (kWh)")
                            eleven_am_kwh = int(eleven_am_kwh)
                            gauge_chart.add('11 am', eleven_am_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 12) and (twelve == False):
                            twelve = True
                            twelve_pm_kwh = interpret_csv("Main (kWh)")
                            if twelve_pm_kwh == '' or twelve_pm_kwh is None:
                                twelve_pm_kwh = interpret_csv("Main (kWh)")
                            twelve_pm_kwh = int(twelve_pm_kwh)
                            gauge_chart.add('12 pm', twelve_pm_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 13) and (one == False):
                            one = True
                            one_pm_kwh = interpret_csv("Main (kWh)")
                            if one_pm_kwh == '' or one_pm_kwh is None:
                                one_pm_kwh = interpret_csv("Main (kWh)")
                            one_pm_kwh = int(one_pm_kwh)
                            gauge_chart.add('1 pm', one_pm_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 14) and (two == False):
                            two = True
                            two_pm_kwh = interpret_csv("Main (kWh)")
                            if two_pm_kwh == '' or two_pm_kwh is None:
                                two_pm_kwh = interpret_csv("Main (kWh)")
                            two_pm_kwh = int(two_pm_kwh)
                            gauge_chart.add('2 pm', two_pm_kwh - six_am_kwh)

                        if (int(currentDT.hour) == 15) and (three == False):
                            three = True
                            three_pm_kwh = interpret_csv("Main (kWh)")
                            if three_pm_kwh == '' or three_pm_kwh is None:
                                three_pm_kwh = interpret_csv("Main (kWh)")
                            three_pm_kwh = int(three_pm_kwh)
                            gauge_chart.add('3 pm', three_pm_kwh - six_am_kwh)

                        gauge_chart.render_to_file("kWhHourly.svg")

            time.sleep(15)

            if int(currentDT.hour) == 23:
                main_kwh_constant = interpret_csv("Main (kWh)")
                while main_kwh_constant == '' or main_kwh_constant is None:
                    main_kwh_constant = interpret_csv("Main (kWh)")
                main_kwh_constant = int(main_kwh_constant)

                gym_kwh_constant = interpret_csv("DG (kWh)")
                while gym_kwh_constant == '' or gym_kwh_constant is None:
                    main_kwh_constant = interpret_csv("Main (kWh)")
                gym_kwh_constant = int(gym_kwh_constant)

                kitchen_kwh_constant = interpret_csv("DE (kWh)")
                while kitchen_kwh_constant == '' or kitchen_kwh_constant is None:
                    kitchen_kwh_constant = 0
                kitchen_kwh_constant = int(kitchen_kwh_constant)

                collins_center_kwh_constant = interpret_csv("AMDP (kWh)")
                while collins_center_kwh_constant == '' or collins_center_kwh_constant is None:
                    collins_center_kwh_constant = 0
                collins_center_kwh_constant = int(collins_center_kwh_constant)
                six = False
                seven = False
                eight = False
                nine = False
                ten = False
                eleven = False
                twelve = False
                one = False
                two = False
                three = False
                six_am_kwh = 0

    except KeyboardInterrupt:
        kW.render_to_file("static/svg/kw.svg")
        kWh.render_to_file("static/svg/kwh.svg")
        dollar.render_to_file("static/svg/dollars.svg")
        if 5 < currentDT.hour < 16:
            gauge_chart.render_to_file("static/svg/kWhHourly.svg")
