#!/usr/bin/env python3
import argparse
import json
import random
from colorama import Fore, Back, Style

# Dictionary of Country to ISO 3166-1 Mappings. Currently only USA because I'm small minded.
country = {
'usa': {'ISO': '840'}
}
# Dictionary of US States and their assoicated:
#     - US Region IDs
#     - US Division IDs
#     - US State FIPS Codes
#     - (See here: https://www.census.gov/geo/reference/gtc/gtc_census_divreg.html)
usa = {
 'Alabama': {'Division': '6', 'Region': '3', 'State FIPS Code': '01'},
 'Alaska': {'Division': '8', 'Region': '4', 'State FIPS Code': '02'},
 'Arizona': {'Division': '7', 'Region': '4', 'State FIPS Code': '04'},
 'Arkansas': {'Division': '6', 'Region': '3', 'State FIPS Code': '05'},
 'California': {'Division': '8', 'Region': '4', 'State FIPS Code': '06'},
 'Colorado': {'Division': '7', 'Region': '4', 'State FIPS Code': '08'},
 'Connecticut': {'Division': '1', 'Region': '1', 'State FIPS Code': '09'},
 'Delaware': {'Division': '5', 'Region': '3', 'State FIPS Code': '10'},
 'District of Columbia': {'Division': '5', 'Region': '3', 'State FIPS Code': '11'},
 'Florida': {'Division': '5', 'Region': '3', 'State FIPS Code': '12'},
 'Georgia': {'Division': '5', 'Region': '3', 'State FIPS Code': '13'},
 'Hawaii': {'Division': '8', 'Region': '4', 'State FIPS Code': '15'},
 'Idaho': {'Division': '7', 'Region': '4', 'State FIPS Code': '16'},
 'Illinois': {'Division': '3', 'Region': '2', 'State FIPS Code': '17'},
 'Indiana': {'Division': '3', 'Region': '2', 'State FIPS Code': '18'},
 'Iowa': {'Division': '4', 'Region': '2', 'State FIPS Code': '19'},
 'Kansas': {'Division': '4', 'Region': '2', 'State FIPS Code': '20'},
 'Kentucky': {'Division': '6', 'Region': '3', 'State FIPS Code': '21'},
 'Louisiana': {'Division': '6', 'Region': '3', 'State FIPS Code': '22'},
 'Maine': {'Division': '1', 'Region': '1', 'State FIPS Code': '23'},
 'Maryland': {'Division': '5', 'Region': '3', 'State FIPS Code': '24'},
 'Massachusetts': {'Division': '1', 'Region': '1', 'State FIPS Code': '25'},
 'Michigan': {'Division': '3', 'Region': '2', 'State FIPS Code': '26'},
 'Minnesota': {'Division': '4', 'Region': '2', 'State FIPS Code': '27'},
 'Mississippi': {'Division': '6', 'Region': '3', 'State FIPS Code': '28'},
 'Missouri': {'Division': '4', 'Region': '2', 'State FIPS Code': '29'},
 'Montana': {'Division': '7', 'Region': '4', 'State FIPS Code': '30'},
 'Nebraska': {'Division': '4', 'Region': '2', 'State FIPS Code': '31'},
 'Nevada': {'Division': '7', 'Region': '4', 'State FIPS Code': '32'},
 'New Hampshire': {'Division': '1', 'Region': '1', 'State FIPS Code': '33'},
 'New Jersey': {'Division': '2', 'Region': '1', 'State FIPS Code': '34'},
 'New Mexico': {'Division': '7', 'Region': '4', 'State FIPS Code': '35'},
 'New York': {'Division': '2', 'Region': '1', 'State FIPS Code': '36'},
 'North Carolina': {'Division': '5', 'Region': '3', 'State FIPS Code': '37'},
 'North Dakota': {'Division': '4', 'Region': '2', 'State FIPS Code': '38'},
 'Ohio': {'Division': '3', 'Region': '2', 'State FIPS Code': '39'},
 'Oklahoma': {'Division': '6', 'Region': '3', 'State FIPS Code': '40'},
 'Oregon': {'Division': '8', 'Region': '4', 'State FIPS Code': '41'},
 'Pennsylvania': {'Division': '2', 'Region': '1', 'State FIPS Code': '42'},
 'Rhode Island': {'Division': '1', 'Region': '1', 'State FIPS Code': '44'},
 'South Carolina': {'Division': '5', 'Region': '3', 'State FIPS Code': '45'},
 'South Dakota': {'Division': '4', 'Region': '2', 'State FIPS Code': '46'},
 'Tennessee': {'Division': '6', 'Region': '3', 'State FIPS Code': '47'},
 'Texas': {'Division': '6', 'Region': '3', 'State FIPS Code': '48'},
 'Utah': {'Division': '7', 'Region': '4', 'State FIPS Code': '49'},
 'Vermont': {'Division': '1', 'Region': '1', 'State FIPS Code': '50'},
 'Virginia': {'Division': '5', 'Region': '3', 'State FIPS Code': '51'},
 'Washington': {'Division': '8', 'Region': '4', 'State FIPS Code': '53'},
 'West Virginia': {'Division': '5', 'Region': '3', 'State FIPS Code': '54'},
 'Wisconsin': {'Division': '3', 'Region': '2', 'State FIPS Code': '55'},
 'Wyoming': {'Division': '7', 'Region': '4', 'State FIPS Code': '56'}
 }
# Generate a random 4 digit number
def random_id():
    for n in range(1):
        return(random.randint(1,9999))

delimeter = '.'
# CRM System (or whatever) identifier. In our case, this maps to a ConnectWise Company RecID
tenant_id = input("CRM ID: ")
# Hard coded to USA. I'm not normally this patriotic
service_country = country['usa']['ISO']
service_type = input("IP Transit [1], MPLS [2], SD-WAN [3]: ")
service_state = input("Location (US State): ")
service_region = usa[str(service_state)]['Region']
service_division = usa[str(service_state)]['Division']
service_statefips = usa[str(service_state)]['State FIPS Code']

# Stringify and/or combine the components into something more usable
circuit_type = str(service_type)
circuit_loc_id = str(service_country + service_region + service_division)
circuit_tenant = str(tenant_id)
circuit_service_id = str(random_id())
# Combine #allthethings
circuit_id = circuit_type + delimeter + circuit_loc_id + delimeter + circuit_tenant + delimeter + circuit_service_id
# Print the generated circuit ID with color
print()
print(Fore.BLUE + 'Your circucit ID is: ', Fore.GREEN, Style.BRIGHT + circuit_id)
print()
