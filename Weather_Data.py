'''
weather data file
'''

def get_relevant_weather_information(forecast_data):
    # Get the value of "mintemp_f"
    mintemp_f = forecast_data['forecast']['forecastday'][0]['day']['mintemp_f']
    print(mintemp_f)
    