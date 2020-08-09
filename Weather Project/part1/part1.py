import json
from datetime import datetime ## Library

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
    ## Arguments                    ##
    ##***************************** ##
    number_items = 0                ## Days
    temps_min = []                  ## Mins
    temps_max = []                  ## Max
    date_list = []                  ## Dates
    sum_output = ""                 ##
    daily_output = ""               ##   
    ##***************************** ##

    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    
        weather = json_data["DailyForecasts"] ### This Is A LIST from json file

        for forecast in weather:
            number_items += 1 ## Keep count of lines of data read to pass to the calculate_mean function later
            daily_date = convert_date(forecast["Date"]) ## Date from nested in DailyForecast data in json file
            date_list.append(daily_date)
            # format_date = f"\n-------- {daily_date} --------\n"

            min_temp = convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]) ## Hold min temp to print in summary of each day
            temps_min.append(min_temp)
            totalMin = sum(temps_min)
            lowestIndex = temps_min.index(min(temps_min))
            lowest_temp = format_temperature(min(temps_min))
            lowestTempDate = date_list[lowestIndex]
            avgMin = format_temperature(calculate_mean(totalMin, number_items))

            max_temp = convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]) ## Hold max temp to print in summary of each day
            temps_max.append(max_temp)
            totalMax = sum(temps_max)
            highestIndex = temps_max.index(max(temps_max))
            highest_temp = format_temperature(max(temps_max))
            highestTempDate = date_list[highestIndex]
            avgMax = format_temperature(calculate_mean(totalMax, number_items))

            DayMessage = (forecast["Day"]["LongPhrase"])
            RainChanceDay = (forecast["Day"]["RainProbability"])
            NightMessage = (forecast["Night"]["LongPhrase"])
            RainChanceNight = (forecast["Night"]["RainProbability"])

            min_temp = format_temperature(min_temp)
            max_temp = format_temperature(max_temp)

            line1 = f"\n-------- {daily_date} --------"
            line2 = f"Minimum Temperature: {min_temp}"
            line3 = f"Maximum Temperature: {max_temp}"
            line4 = f"Daytime: {DayMessage}"
            line5 = f"    Chance of rain:  {RainChanceDay}%"
            line6 = f"Nighttime: {NightMessage}"
            line7 = f"    Chance of rain:  {RainChanceNight}%"
            daily_output += line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 + "\n"

        ## Print a summary of the forecast 
        sum_output += f"{number_items} Day Overview\n"
        sum_output += f"    The lowest temperature will be {lowest_temp}, and will occur on {lowestTempDate}.\n"
        sum_output += f"    The highest temperature will be {highest_temp}, and will occur on {highestTempDate}.\n"
        sum_output += f"    The average low this week is {avgMin}.\n"
        sum_output += f"    The average high this week is {avgMax}.\n"

    formatted_data = sum_output + daily_output + "\n"
    return formatted_data
#*******************************************************************##

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_8days.json"))

#*-------*#
# The End #
#*-------*#





