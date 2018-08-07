import pygal
import argparse
import pandas as pd
import time
import datetime
import os
from bacnet_gateway_requests import get_value_and_units

def myFunction(facility):
    try:
        # Get hostname and port of BACnet Gateway
        parser = argparse.ArgumentParser(description='Test BACnet Gateway', add_help=False)
        parser.add_argument('-h', dest='hostname')
        parser.add_argument('-p', dest='port')
        args = parser.parse_args()

        # Read spreadsheet into a dataframe.
        # Each row contains the following:
        #   - Feeder
        #   - Instance ID of electric meter
        df = pd.read_csv('../csv/ahs_elec.csv')

        # Iterate over the rows of the dataframe, getting meter readings for each feeder
        for index, row in df.iterrows():
            if facility!=row['Label']:
                continue
            # Retrieve data
            value, units = get_value_and_units(row['Facility'], row['Meter'], args.hostname, args.port)

            # Prepare to print
            value = int(value) if value else ''

            # Output CSV format
            if facility == row['Label']:
                return (value)
                print(value)

    except KeyboardInterrupt:
        print('Bye')
        import sys
        sys.exit()
gauge_chart = pygal.Gauge(human_readable=True)

mainkWhConstant=myFunction("Main (kWh)")
if mainkWhConstant=='':
    mainkWhConstant=0
mainkWhConstant=int(mainkWhConstant)

gymkWhConstant = myFunction("DG (kWh)")
if gymkWhConstant == '':
    gymkWhConstant = 0
gymkWhConstant = int(gymkWhConstant)

kitchenkWhConstant = myFunction("DE (kWh)")
if kitchenkWhConstant == '':
    kitchenkWhConstant = 0
kitchenkWhConstant = int(kitchenkWhConstant)

collinscenterkWhConstant = myFunction("AMDP (kWh)")
if collinscenterkWhConstant == '':
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

try:

    percent_formatter = lambda x: '{:.10g}%'.format(x)
    dollar_formatter = lambda x: '{:.10g}$'.format(x)
    kW_formatter = lambda x: '{:.10g}kW'.format(x)
    kWh_formatter = lambda x: '{:.10g}kWh'.format(x)
    while True:

        currentDT = datetime.datetime.now()

        mainkW=myFunction("Main (kW)")
        if mainkW=='':
            mainkW=0
        mainkW=int(mainkW)

        mainkWh=myFunction("Main (kWh)")
        if mainkWh=='':
            mainkWh=0
        mainkWh=int(mainkWh)
        mainkWh=mainkWh-mainkWhConstant

        gymkW = myFunction("DG (kW)")
        if gymkW == '':
            gymkW = 0
        gymkW = int(gymkW)

        gymkWh = myFunction("DG (kWh)")
        if gymkWh == '':
            gymkWh = 0
        gymkWh = int(gymkWh)
        gymkWh=gymkWh-gymkWhConstant

        kitchenkW = myFunction("DE (kW)")
        if kitchenkW == '':
            kitchenkW = 0
        kitchenkW = int(kitchenkW)

        kitchenkWh = myFunction("DE (kWh)")
        if kitchenkWh == '':
            kitchenkWh = 0
        kitchenkWh = int(kitchenkWh)
        kitchenkWh=kitchenkWh-kitchenkWhConstant

        collinscenterkW = myFunction("AMDP (kW)")
        if collinscenterkW == '':
            collinscenterkW = 0
        collinscenterkW = int(collinscenterkW)

        collinscenterkWh = myFunction("AMDP (kWh)")
        if collinscenterkWh == '':
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
        while currentDT.hour==5:
            gauge_chart.title = 'Electricity used hourly in kWh all of ahs'
            gauge_chart.range = [0, 7000]
        if (int(currentDT.hour)==6) and (six==False):
            six=True
            gauge_chart.add('6 am', 0)
            sixamkWh = myFunction("Main (kWh)")
            if sixamkWh == '':
                sixamkWh = myFunction("Main (kWh)")
            sixamkWh = int(sixamkWh)

        if (int(currentDT.hour)==7) and (seven==False):
            seven=True
            sevenamkWh = myFunction("Main (kWh)")
            if sevenamkWh == '':
                sevenamkWh = myFunction("Main (kWh)")
            sevenamkWh = int(sevenamkWh)
            gauge_chart.add('7 am', sevenamkWh-sixamkWh)

        if (int(currentDT.hour)==8) and (eight==False):
            eight=True
            eightamkWh = myFunction("Main (kWh)")
            if eightamkWh == '':
                eightamkWh = myFunction("Main (kWh)")
            eightamkWh = int(eightamkWh)
            gauge_chart.add('8 am', eightamkWh-sixamkWh)

        if (int(currentDT.hour)==9) and (nine==False):
            nine=True
            nineamkWh = myFunction("Main (kWh)")
            if nineamkWh == '':
                nineamkWh = myFunction("Main (kWh)")
            nineamkWh = int(nineamkWh)
            gauge_chart.add('9 am', nineamkWh-sixamkWh)

        if (int(currentDT.hour)==10) and (ten==False):
            ten=True
            tenamkWh = myFunction("Main (kWh)")
            if tenamkWh == '':
                tenamkWh = myFunction("Main (kWh)")
            tenamkWh = int(tenamkWh)
            gauge_chart.add('10 am', tenamkWh-sixamkWh)

        if (int(currentDT.hour) == 11) and (eleven == False):
            eleven = True
            elevenamkWh = myFunction("Main (kWh)")
            if elevenamkWh == '':
                elevenamkWh = myFunction("Main (kWh)")
            elevenamkWh = int(elevenamkWh)
            gauge_chart.add('11 am', elevenamkWh - sixamkWh)

        if (int(currentDT.hour) == 12) and (twelve == False):
            twelve = True
            twelvepmkWh = myFunction("Main (kWh)")
            if twelvepmkWh == '':
                twelvepmkWh = myFunction("Main (kWh)")
            twelvepmkWh = int(twelveamkWh)
            gauge_chart.add('12 pm', twelvepmkWh - sixamkWh)

        if (int(currentDT.hour) == 13) and (one == False):
            one = True
            onepmkWh = myFunction("Main (kWh)")
            if onepmkWh == '':
                onepmkWh = myFunction("Main (kWh)")
            onepmkWh = int(onepmkWh)
            gauge_chart.add('1 pm', onepmkWh - sixamkWh)

        if (int(currentDT.hour) == 14) and (two == False):
            two = True
            twopmkWh = myFunction("Main (kWh)")
            if twopmkWh == '':
                twopmkWh = myFunction("Main (kWh)")
            twopmkWh = int(twopmkWh)
            gauge_chart.add('2 pm', twopmkWh - sixamkWh)

        if (int(currentDT.hour) == 15) and (three == False):
            three = True
            threepmkWh = myFunction("Main (kWh)")
            if threepmkWh == '':
                threepmkWh = myFunction("Main (kWh)")
            threepmkWh = int(threepmkWh)
            gauge_chart.add('3 pm', threepmkWh - sixamkWh)

        gauge_chart.render_to_file("kWhHourly.svg")

        time.sleep(15)

        if (int(currentDT.hour) == 23):
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
            os.remove("kWhHourly.svg")
            sixamkWh = 0


except KeyboardInterrupt:
    kW.render_to_file("kw.svg")
    kWh.render_to_file("kwh.svg")
    dollar.render_to_file("dollars.svg")
    if currentDT.hour > 5 and currentDT.hour < 16:
        gauge_chart.render_to_file("kWhHourly.svg")