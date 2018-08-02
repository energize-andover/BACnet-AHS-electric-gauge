# Welcome to BACnet Electric Gauge for AHS

Hi!

I'm Ayush Zenith. A high school sophomore from Andover High School, Andover, Massachusetts and this page is about an application I built with the help of a friend, Samar Seth.

To learn more about me check out my [blog](https://ayushenergyproject.weebly.com/).

## How to run the server
1. Clone or Download BACnet-AHS-electric-gauge
2. Run Main.py
3. Wait for 30 seconds for buffer/reload/connectivity time
4. Open index.html in your browser
**Note - file index.html would be the start up file for any apache configuration and documentroot would be .py**

## About the Application

### One word summary of the application?
Simply put 'Gauges'

### What is the application about?
The application in its current stage basically a live gauge for monitering electricity usage around Andover High School. 

### The application currently consists of four gauges each being:
1. AHS Main(Power usage for all of AHS)
2. AHS GYM(Power usage for the gym's)
3. AHS Colins Center(Power usage for the collins center building)
4. AHS Kitchen(Power usage for the kitchen)

### The application currently measures electricity in:
1. kW(Kilowatt)
2. kWh(Kilowatt hour)(Starts to calculate the kWh since the server has been running)
3. Cost $$(Cost in dollars)(Starts to calculate the dollars since the server has been running)

### What are the technologies implimented
1. Python
2. BACnet
3. HTML
4. CSS
5. JS
6. SVG
7. Pandas
8. Pygal

## In depth explanations of each file
1. Main.py
  * Main.py is the file that is going to be run on the server hosting the website.
  * Main.py is the back end for the server
  * Main.py has a function called 'myFunction()' that takes in a String. The String being the location and the unit the user would like their data from the BACnet server.
    * Ex-"Main (kWh)"
  * Main.py takes the values the BACnet server returns and uses the pygal library to generate half solid gauges.
  * The pygal library then take the values and generates a .svg file with the solid gauges in it.
2. bacnet_gateway_requests.py
  * This is just one of the files that the BACnet API needs
3. ahs_elec.csv
  * This is just one of the files that the BACnet API needs
4. index.html
  * This is one of the three HTML files that make up our web application
  * This file in named index.html for easy configuration with apache
  * This file is shows the electricity used in kilowatts
  * Noteable things about the file:
    * the line ```<meta http-equiv="refresh" content="15">``` forces the html page refresh every 15 seconds to refresh the data it has
    * There are 3 buttons on the side with functions:
      * kW opens up index.html
      * kWh opens up kWh.html
      * Cost $$ opens up dollars.html
    * The gauges in the center are svg files that pygal makes and when the page refreshes it looks for the new svg file pygal generated for us and displays that with the new data
5. kWh.html
  * This is one of the three HTML files that make up our web application
  * This file in named kWh.html because it shows the electricity used in kilowatt hours
  * It starts to calculate kWh used since Main.py started to run
  * Noteable things about the file:
    * the line ```<meta http-equiv="refresh" content="15">``` forces the html page refresh every 15 seconds to refresh the data it has
    * There are 3 buttons on the side with functions:
      * kW opens up index.html
      * kWh opens up kWh.html
      * Cost $$ opens up dollars.html
    * The gauges in the center are svg files that pygal makes and when the page refreshes it looks for the new svg file pygal generated for us and displays that with the new data
6. dollars.html
  * This is one of the three HTML files that make up our web application
  * This file in named dollars.html because it shows the electricity used in dollars or cost
  * It starts to calculate cost used since Main.py started to run
  * Noteable things about the file:
    * the line ```<meta http-equiv="refresh" content="15">``` forces the html page refresh every 15 seconds to refresh the data it has
    * There are 3 buttons on the side with functions:
      * kW opens up index.html
      * kWh opens up kWh.html
      * Cost $$ opens up dollars.html
    * The gauges in the center are svg files that pygal makes and when the page refreshes it looks for the new svg file pygal generated for us and displays that with the new data
7. kw.svg
  * This is one of the svg's generated/rendered by pygal
8. kwh.svg
  * This is one of the svg's generated/rendered by pygal
7. dollars.svg
  * This is one of the svg's generated/rendered by pygal

## Graphics
1. In every solid gauge the amount of electricity is written below
2. When the cursor is taken over one of the solid gauges it displays the amount of electricity used in a nice cool box.
3. When cursor is taken over the buttons they change color and the cursor changes too
4. Gauges can be hidden by clicking the key in the left

## Issues in current version
1. The page refreshes every 15 seconds resettign any kind of zoom that might have been set or resetting any graphics with the gauges

## Future updates
1. Currently working on making a full big 360 gauge that has 10 pointers each appearing at every hour interval to see how much electricity was used in every hour.


## Screenshots
![Screenshotone](https://github.com/ayushzenith/BACnet-AHS-electric-gauge/blob/master/Photos/Screen%20Shot%202018-08-01%20at%2011.13.51%20PM.png)
![Screenshottwo](https://github.com/ayushzenith/BACnet-AHS-electric-gauge/blob/master/Photos/Screen%20Shot%202018-08-01%20at%2011.13.54%20PM.png)
![Screenshotthree](https://github.com/ayushzenith/BACnet-AHS-electric-gauge/blob/master/Photos/Screen%20Shot%202018-08-01%20at%2011.16.38%20PM.png)
![Screenshotfour](https://github.com/ayushzenith/BACnet-AHS-electric-gauge/blob/master/Photos/Screen%20Shot%202018-08-01%20at%2011.17.08%20PM.png)
![Screenshotfive](https://github.com/ayushzenith/BACnet-AHS-electric-gauge/blob/master/Photos/Screen%20Shot%202018-08-01%20at%2011.17.42%20PM.png)


## Support or Contact

Contact me
* Ayush Zenith
  * ayushp.zenith@gmail.com
  * [blog](https://ayushenergyproject.weebly.com/).

