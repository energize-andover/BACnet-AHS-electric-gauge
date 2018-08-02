import pygal
import argparse
import pandas as pd
import time
from py.bacnet_gateway_requests import get_value_and_units

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
try:

    percent_formatter = lambda x: '{:.10g}%'.format(x)
    dollar_formatter = lambda x: '{:.10g}$'.format(x)
    kW_formatter = lambda x: '{:.10g}kW'.format(x)
    kWh_formatter = lambda x: '{:.10g}kWh'.format(x)
    while True:

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
        kW.add('AHS MAIN aka all of AHS', [{'value': mainkW, 'max_value': 7000}],
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
        kWh.add('AHS MAIN aka all of AHS', [{'value': mainkWh, 'max_value': 25}],
                  formatter=kWh_formatter)
        kWh.add('AHS GYM', [{'value': gymkWh, 'max_value': 10}],
                  formatter=kWh_formatter)
        kWh.add('AHS COLLINS CENTER', [{'value': collinscenterkWh, 'max_value': 10}],
                  formatter=kWh_formatter)
        kWh.add('AHS KITCHEN', [{'value': kitchenkWh, 'max_value': 10}],
                  formatter=kWh_formatter)
        kWh.render_to_file("kwh.svg")

        dollar = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
                               style=pygal.style.styles['default'](value_font_size=10))
        dollar.add('AHS MAIN aka all of AHS', [{'value': int(mainkWh*0.12), 'max_value': int(0.12*25)}],
                formatter=dollar_formatter)
        dollar.add('AHS GYM', [{'value': int(gymkWh*0.12), 'max_value': int(0.12*10)}],
                formatter=dollar_formatter)
        dollar.add('AHS COLLINS CENTER', [{'value': int(0.12*collinscenterkWh), 'max_value': int(0.12*10)}],
                formatter=dollar_formatter)
        dollar.add('AHS KITCHEN', [{'value': int(0.12*kitchenkWh), 'max_value': int(0.12*10)}],
                formatter=dollar_formatter)
        dollar.render_to_file("dollars.svg")
        time.sleep(10)

except KeyboardInterrupt:
    kW.render_to_file("kw.svg")
    kWh.render_to_file("kwh.svg")
    dollar.render_to_file("dollars.svg")