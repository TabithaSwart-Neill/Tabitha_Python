import json
import plotly.express as px

from datetime import datetime
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

##*******************************************************************************##
# Function below accepts a temperature and returns it with degree symbol         ##
##*******************************************************************************##
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"                                              ##
##                                                                               ##
def format_temperature(temp):                                                    ##
    """Takes a temperature and returns a string with degrees and celcius symbols.##
    Args:                                                                        ##
        temp: A string representing a temperature.                               ##
    Returns:                                                                     ##
        A string contain the temperature and "degrees celcius."                  ##
    """                                                                          ##
    return (f"{temp}{DEGREE_SYBMOL}")                                            ##
##*******************************************************************************##

##*******************************************************************##
##                                                                   ##
## The function below will use an algorytm from docs.python.org      ##
##      https://docs.python.org/3/library/datetime.html              ##
##                                                                   ##
##*******************************************************************##
def convert_date(iso_string):                                        ##
    """Converts an ISO formatted date into a human readable format.  ##
    Args:                                                            ##
        iso_string: An ISO date string..                             ##
    Returns:                                                         ##
        A date formatted like: Weekday Date Month Year               ##
    """                                                              ##
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")         ##
    return d.strftime("%A %d %B %Y")                                 ##
##*******************************************************************##

##*******************************************************************##
# Convert Temperature and pass value to function in print statement  ##
##*******************************************************************##
def convert_f_to_c(temp_in_farenheit):                               ##
    """Converts an temperature from farenheit to celcius             ##
    Args:                                                            ##
        temp_in_farenheit: integer representing a temperature.       ##
    Returns:                                                         ##
        An integer representing a temperature in degrees celcius.    ##
    """                                                              ##
    celsiustemp = round((temp_in_farenheit - 32) *  5/9, 1)          ##
    return celsiustemp                                               ##
##*******************************************************************##

##*******************************************************************##
##                                                                   ##
## Function below accepts total of temperatures                      ##
#  and number of temperatures counted to return average temperature  ##
##                                                                   ##
##*******************************************************************##
def calculate_mean(total, num_items):
    """Calculates the mean.
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = float(total)/ num_items
    mean = round(mean,1)
    return mean

##*************************************************##
## This function will open and read json file      ##
## The function below will do main processing      ##
##*************************************************##
def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    ##******************************##
    ## Lists and variables          ##
    ##***************************** ##
    col_date = []
    min_temp_data = []
    max_temp_data = []
    real_feel_data = []
    real_feel_shade_data = []
    # forecast_file = "data/forecast_5days_b.json"

    # read in data
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
        weather = json_data["DailyForecasts"] ### This Is A LIST from json file
    # for loop
    for item in weather:
        date = item["Date"]# get date from json file
        col_date.append(convert_date(date))# append date to the list

        minimum_daily_temperature = (item["Temperature"]["Minimum"]["Value"])# get min temp from json file
        min_temp_data.append(convert_f_to_c(minimum_daily_temperature))# convert and append to the list

        maximum_daily_temperature = (item["Temperature"]["Maximum"]["Value"])# get max temp from json file
        max_temp_data.append(convert_f_to_c(maximum_daily_temperature))# convert and append to the list

        minimum_realfeel_temperature = (item["RealFeelTemperatureShade"]["Maximum"]["Value"])# get max real feel
        real_feel_data.append(convert_f_to_c(minimum_realfeel_temperature))# convert and append to the list

        minimum_realfeel_shade_temperature = (item["RealFeelTemperature"]["Minimum"]["Value"])# get min real feel
        real_feel_shade_data.append(convert_f_to_c(minimum_realfeel_shade_temperature))# convert and append to the list

    ## Dataframe
    df = {
        "date": col_date,
        "minimum_daily_temperature": min_temp_data,
        "maximum_daily_temperature": max_temp_data,
        "minimum_realfeel_temperature": real_feel_data,
        "minimum_realfeel_shade_temperature": real_feel_shade_data
    }

    ## Set src for Y and X Data for Daily Temps
    fig = px.bar(
        df, 
        y=["minimum_daily_temperature", "maximum_daily_temperature"], 
        x="date"
    )
    fig.update_layout(
        title="Daily Minimum and Maximum Temperatures",
        xaxis_title="Date",
        yaxis_title="Temperature in Degrees Celcius",
        legend_title="Minimums:",
        legend=dict(
                x=1,
                y=1,
                traceorder="reversed",
                title_font_family="Times New Roman",
                font=dict(
                    family="PT Sans Narrow",
                    size=12,
                    color="black"
                ),
                bgcolor="LightSteelBlue",
                bordercolor="Black",
                borderwidth=2
            ),
        font=dict(
            family="PT Sans Narrow",
            size=18,
            color="#9009bd"
        )
    )
    fig.show()

    ## Set src for Y and X Data for Minimum Temps
    fig = px.bar(
        df, 
        y=["minimum_daily_temperature", "minimum_realfeel_temperature", "minimum_realfeel_shade_temperature"], 
        x="date"
    )
    fig.update_layout(
        title="Daily Minimum Temperatures.",
        xaxis_title="Date",
        yaxis_title="Temperature in Degrees Celcius",
        legend_title="Minimums:",
        legend=dict(
                x=1,
                y=1,
                traceorder="reversed",
                title_font_family="Times New Roman",
                font=dict(
                    family="PT Sans Narrow",
                    size=12,
                    color="black"
                ),
                bgcolor="LightSteelBlue",
                bordercolor="Black",
                borderwidth=2
            ),
        font=dict(
            family="PT Sans Narrow",
            size=18,
            color="#9009bd"
        )
    )
    fig.show()
    return

process_weather("data/forecast_8days.json")