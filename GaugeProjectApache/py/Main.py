import pygal
import argparse
import pandas as pd
import time
from building_data_requests import get_value
import numbers
from datetime import timedelta
import datetime

def myFunction(facility):
    try:
        # Read spreadsheet into a dataframe.
        # Each row contains the following:
        #   - Label
        #   - Facility
        #   - Instance ID of electric meter
        df = pd.read_csv('../csv/ahs_power.csv')

        # Output column headings
        print('Feeder,Meter,Units')

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
                print(facility+value)
                print(test)

    except KeyboardInterrupt:
        print('Bye')
        import sys
        sys.exit()
gauge_chart = pygal.Gauge(human_readable=True)

mainkWhConstant=myFunction("Main (kWh)")
while mainkWhConstant=='' or mainkWhConstant is None:
    mainkWhConstant=0
mainkWhConstant=int(mainkWhConstant)

gymkWhConstant = myFunction("DG (kWh)")
while gymkWhConstant == '' or gymkWhConstant is None:
    gymkWhConstant = 0
gymkWhConstant = int(gymkWhConstant)

kitchenkWhConstant = myFunction("DE (kWh)")
while kitchenkWhConstant == '' or kitchenkWhConstant is None:
    kitchenkWhConstant = 0
kitchenkWhConstant = int(kitchenkWhConstant)

collinscenterkWhConstant = myFunction("AMDP (kWh)")
while collinscenterkWhConstant == '' or collinscenterkWhConstant is None:
    collinscenterkWhConstant = 0
collinscenterkWhConstant = int(collinscenterkWhConstant)

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

        mainkW=myFunction("Main (kW)")
        if mainkW=='' or mainkW is None:
            mainkW=0
        mainkW=int(mainkW)

        mainkWh=myFunction("Main (kWh)")
        if mainkWh=='' or mainkWh is None:
            mainkWh=0
        mainkWh=int(mainkWh)
        mainkWh=mainkWh-mainkWhConstant

        gymkW = myFunction("DG (kW)")
        if gymkW == '' or gymkW is None:
            gymkW = 0
        gymkW = int(gymkW)

        gymkWh = myFunction("DG (kWh)")
        if gymkWh == '' or gymkWh is None:
            gymkWh = 0
        gymkWh = int(gymkWh)
        gymkWh=gymkWh-gymkWhConstant

        kitchenkW = myFunction("DE (kW)")
        if kitchenkW == '' or kitchenkW is None:
            kitchenkW = 0
        kitchenkW = int(kitchenkW)

        kitchenkWh = myFunction("DE (kWh)")
        if kitchenkWh == '' or kitchenkWh is None:
            kitchenkWh = 0
        kitchenkWh = int(kitchenkWh)
        kitchenkWh=kitchenkWh-kitchenkWhConstant

        collinscenterkW = myFunction("AMDP (kW)")
        if collinscenterkW == '' or collinscenterkW is None:
            collinscenterkW = 0
        collinscenterkW = int(collinscenterkW)

        collinscenterkWh = myFunction("AMDP (kWh)")
        if collinscenterkWh == '' or collinscenterkWh is None:
            collinscenterkWh = 0
        collinscenterkWh = int(collinscenterkWh)
        collinscenterkWh=collinscenterkWh-collinscenterkWh

        kW = pygal.SolidGauge(
            half_pie=True, inner_radius=0.70,
            style=pygal.style.styles['default'](value_font_size=10))
        kW.add('AHS MAIN aka all of AHS', [{'value': mainkW, 'max_value': 750}],
                  formatter=kW_formatter)
        kW.add('AHS GYM', [{'value': gymkW, 'max_value': 200}],
                  formatter=kW_formatter)
        kW.add('AHS COLLINS CENTER', [{'value': collinscenterkW, 'max_value': 250}],
                  formatter=kW_formatter)
        kW.add('AHS KITCHEN', [{'value': kitchenkW, 'max_value': 150}],
                  formatter=kW_formatter)
        kW.render_to_file("kw.svg")

        kWh = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
            style=pygal.style.styles['default'](value_font_size=10))
        kWh.add('AHS MAIN aka all of AHS', [{'value': mainkWh, 'max_value': 50}],
                  formatter=kWh_formatter)
        kWh.add('AHS GYM', [{'value': gymkWh, 'max_value': 20}],
                  formatter=kWh_formatter)
        kWh.add('AHS COLLINS CENTER', [{'value': collinscenterkWh, 'max_value': 20}],
                  formatter=kWh_formatter)
        kWh.add('AHS KITCHEN', [{'value': kitchenkWh, 'max_value': 20}],
                  formatter=kWh_formatter)
        kWh.render_to_file("kwh.svg")

        dollar = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
                               style=pygal.style.styles['default'](value_font_size=10))
        dollar.add('AHS MAIN aka all of AHS', [{'value': int(mainkWh*0.12), 'max_value': int(0.12*50)}],
                formatter=dollar_formatter)
        dollar.add('AHS GYM', [{'value': int(gymkWh*0.12), 'max_value': int(0.12*20)}],
                formatter=dollar_formatter)
        dollar.add('AHS COLLINS CENTER', [{'value': int(0.12*collinscenterkWh), 'max_value': int(0.12*20)}],
                formatter=dollar_formatter)
        dollar.add('AHS KITCHEN', [{'value': int(0.12*kitchenkWh), 'max_value': int(0.12*20)}],
                formatter=dollar_formatter)
        dollar.render_to_file("dollars.svg")
        if currentDT.hour == 23:
            currentday = currentDT2.day+timedelta(days=1)
        try:
            currentday
        except NameError:
            print("kWh hourly not ready yet")
        else:
            if currentDT2.day == currentday:
                if currentDT.hour>=5 and currentDT.hour<16:
                    if (int(currentDT.hour)==6) and (six==False):
                        six=True
                        gauge_chart.add('6 am', 0)
                        sixamkWh = myFunction("Main (kWh)")
                        if sixamkWh == '' or sixamkWh is None:
                            sixamkWh = myFunction("Main (kWh)")
                        sixamkWh = int(sixamkWh)

                    if (int(currentDT.hour)==7) and (seven==False):
                        seven=True
                        sevenamkWh = myFunction("Main (kWh)")
                        if sevenamkWh == '' or sevenamkWh is None:
                            sevenamkWh = myFunction("Main (kWh)")
                        sevenamkWh = int(sevenamkWh)
                        gauge_chart.add('7 am', sevenamkWh-sixamkWh)

                    if (int(currentDT.hour)==8) and (eight==False):
                        eight=True
                        eightamkWh = myFunction("Main (kWh)")
                        if eightamkWh == '' or eightamkWh is None:
                            eightamkWh = myFunction("Main (kWh)")
                        eightamkWh = int(eightamkWh)
                        gauge_chart.add('8 am', eightamkWh-sixamkWh)

                    if (int(currentDT.hour)==9) and (nine==False):
                        nine=True
                        nineamkWh = myFunction("Main (kWh)")
                        if nineamkWh == '' or nineamkWh is None:
                            nineamkWh = myFunction("Main (kWh)")
                        nineamkWh = int(nineamkWh)
                        gauge_chart.add('9 am', nineamkWh-sixamkWh)

                    if (int(currentDT.hour)==10) and (ten==False):
                        ten=True
                        tenamkWh = myFunction("Main (kWh)")
                        if tenamkWh == '' or tenamkWh is None:
                            tenamkWh = myFunction("Main (kWh)")
                        tenamkWh = int(tenamkWh)
                        gauge_chart.add('10 am', tenamkWh-sixamkWh)

                    if (int(currentDT.hour) == 11) and (eleven == False):
                        eleven = True
                        elevenamkWh = myFunction("Main (kWh)")
                        if elevenamkWh == '' or elevenamkWh is None:
                            elevenamkWh = myFunction("Main (kWh)")
                        elevenamkWh = int(elevenamkWh)
                        gauge_chart.add('11 am', elevenamkWh - sixamkWh)

                    if (int(currentDT.hour) == 12) and (twelve == False):
                        twelve = True
                        twelvepmkWh = myFunction("Main (kWh)")
                        if twelvepmkWh == '' or twelvepmkWh is None:
                            twelvepmkWh = myFunction("Main (kWh)")
                        twelvepmkWh = int(twelvepmkWh)
                        gauge_chart.add('12 pm', twelvepmkWh - sixamkWh)

                    if (int(currentDT.hour) == 13) and (one == False):
                        one = True
                        onepmkWh = myFunction("Main (kWh)")
                        if onepmkWh == '' or onepmkWh is None:
                            onepmkWh = myFunction("Main (kWh)")
                        onepmkWh = int(onepmkWh)
                        gauge_chart.add('1 pm', onepmkWh - sixamkWh)

                    if (int(currentDT.hour) == 14) and (two == False):
                        two = True
                        twopmkWh = myFunction("Main (kWh)")
                        if twopmkWh == '' or twopmkWh is None:
                            twopmkWh = myFunction("Main (kWh)")
                        twopmkWh = int(twopmkWh)
                        gauge_chart.add('2 pm', twopmkWh - sixamkWh)

                    if (int(currentDT.hour) == 15) and (three == False):
                        three = True
                        threepmkWh = myFunction("Main (kWh)")
                        if threepmkWh == '' or threepmkWh is None:
                            threepmkWh = myFunction("Main (kWh)")
                        threepmkWh = int(threepmkWh)
                        gauge_chart.add('3 pm', threepmkWh - sixamkWh)

                    gauge_chart.render_to_file("kWhHourly.svg")

        time.sleep(15)

        if (int(currentDT.hour) == 23):
            mainkWhConstant = myFunction("Main (kWh)")
            while mainkWhConstant == '' or mainkWhConstant is None:
                mainkWhConstant = myFunction("Main (kWh)")
            mainkWhConstant = int(mainkWhConstant)

            gymkWhConstant = myFunction("DG (kWh)")
            while gymkWhConstant == '' or gymkWhConstant is None:
                mainkWhConstant = myFunction("Main (kWh)")
            gymkWhConstant = int(gymkWhConstant)

            kitchenkWhConstant = myFunction("DE (kWh)")
            while kitchenkWhConstant == '' or kitchenkWhConstant is None:
                kitchenkWhConstant = 0
            kitchenkWhConstant = int(kitchenkWhConstant)

            collinscenterkWhConstant = myFunction("AMDP (kWh)")
            while collinscenterkWhConstant == '' or collinscenterkWhConstant is None:
                collinscenterkWhConstant = 0
            collinscenterkWhConstant = int(collinscenterkWhConstant)
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
            sixamkWh = 0


except KeyboardInterrupt:
    kW.render_to_file("kw.svg")
    kWh.render_to_file("kwh.svg")
    dollar.render_to_file("dollars.svg")
    if currentDT.hour > 5 and currentDT.hour < 16:
        gauge_chart.render_to_file("kWhHourly.svg")