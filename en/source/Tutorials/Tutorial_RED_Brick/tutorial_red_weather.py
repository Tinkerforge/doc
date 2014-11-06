#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywapi
from unidecode import unidecode

location = u"Stukenbrock"
#location = u"Bielefeld"

location_id = pywapi.get_location_ids(location).keys()[0]

weather_com_result = pywapi.get_weather_from_weather_com(location_id)
print weather_com_result['current_conditions']
 
print ("Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + u"°C now in " + location + ".")
