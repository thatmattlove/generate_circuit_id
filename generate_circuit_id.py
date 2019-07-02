#!/usr/bin/env python
"""
Generates a circuit ID based on input parameters. Matches input state
to list of states and their attributes, combines with customer ID and
service type. Then generates a random 4 digit number and forms one
id number. Example:

1.84047.12345.1697

"""
# Standard Library Imports
import random

# Third Party Imports
import click

# Set of Country to ISO 3166-1 Mappings. Currently only USA because I'm small minded.
countries = {("usa", "840")}

# Set of US States and their assoicated:
#     - US Region IDs
#     - US Division IDs
#     - US State FIPS Codes
#     - (See here: https://www.census.gov/geo/reference/gtc/gtc_census_divreg.html)

usa = {
    ("Alabama", "AL", ("6", "3", "01")),
    ("Alaska", "AK", ("8", "4", "02")),
    ("Arizona", "AZ", ("7", "4", "04")),
    ("Arkansas", "AR", ("6", "3", "05")),
    ("California", "CA", ("8", "4", "06")),
    ("Colorado", "CO", ("7", "4", "08")),
    ("Connecticut", "CT", ("1", "1", "09")),
    ("Delaware", "DE", ("5", "3", "10")),
    ("District of Columbia", "DC", ("5", "3", "11")),
    ("Florida", "FL", ("5", "3", "12")),
    ("Georgia", "GA", ("5", "3", "13")),
    ("Hawaii", "HI", ("8", "4", "15")),
    ("Idaho", "ID", ("7", "4", "16")),
    ("Illinois", "IL", ("3", "2", "17")),
    ("Indiana", "IN", ("3", "2", "18")),
    ("Iowa", "IA", ("4", "2", "19")),
    ("Kansas", "KS", ("4", "2", "20")),
    ("Kentucky", "KY", ("6", "3", "21")),
    ("Louisiana", "LA", ("6", "3", "22")),
    ("Maine", "ME", ("1", "1", "23")),
    ("Maryland", "MD", ("5", "3", "24")),
    ("Massachusetts", "MA", ("1", "1", "25")),
    ("Michigan", "MI", ("3", "2", "26")),
    ("Minnesota", "MN", ("4", "2", "27")),
    ("Mississippi", "MS", ("6", "3", "28")),
    ("Missouri", "MO", ("4", "2", "29")),
    ("Montana", "MT", ("7", "4", "30")),
    ("Nebraska", "NE", ("4", "2", "31")),
    ("Nevada", "NV", ("7", "4", "32")),
    ("New Hampshire", "NH", ("1", "1", "33")),
    ("New Jersey", "NJ", ("2", "1", "34")),
    ("New Mexico", "NM", ("7", "4", "35")),
    ("New York", "NY", ("2", "1", "36")),
    ("North Carolina", "NC", ("5", "3", "37")),
    ("North Dakota", "ND", ("4", "2", "38")),
    ("Ohio", "OH", ("3", "2", "39")),
    ("Oklahoma", "OK", ("6", "3", "40")),
    ("Oregon", "OR", ("8", "4", "41")),
    ("Pennsylvania", "PA", ("2", "1", "42")),
    ("Rhode Island", "RI", ("1", "1", "44")),
    ("South Carolina", "SC", ("5", "3", "45")),
    ("South Dakota", "SD", ("4", "2", "46")),
    ("Tennessee", "TN", ("6", "3", "47")),
    ("Texas", "TX", ("6", "3", "48")),
    ("Utah", "UT", ("7", "4", "49")),
    ("Vermont", "VT", ("1", "1", "50")),
    ("Virginia", "VA", ("5", "3", "51")),
    ("Washington", "WA", ("8", "4", "53")),
    ("West Virginia", "WV", ("5", "3", "54")),
    ("Wisconsin", "WI", ("3", "2", "55")),
    ("Wyoming", "WY", ("7", "4", "56")),
}

# Generate a random 4 digit number
random_id = lambda: "{:04}".format(random.randrange(1, 10 ** 4))


def match_country_id(country_name):
    """
    Searches input country name against list of countries, returns
    match
    """
    matched_country = None
    for country in countries:
        if country[0] == country_name:
            matched_country = country[1]
    if not matched_country:
        raise click.ClickException("{} did not match any configured countries.").format(
            country_name
        )
    return matched_country


def match_state(state_name):
    """
    Searches input state name/abbrevation against list of states,
    returns match
    """
    state_info = None
    for state in usa:
        if state[0].lower() == state_name.lower():
            state_info = state[2]
        elif state[1].lower() == state_name.lower():
            state_info = state[2]
    if not state_info:
        raise click.ClickException(
            "Unable to match state for input {}".format(state_name)
        )
    return state_info


@click.command()
@click.option(
    "-c",
    "--customer-id",
    "customer_id",
    prompt="CRM ID",
    required=True,
    type=int,
    help="Customer ID Number from CRM",
)
@click.option(
    "-s",
    "--state",
    "search_state",
    prompt="US State",
    required=True,
    help="US State Where Service is Delivered",
)
@click.option(
    "-t",
    "--type",
    "service_type",
    prompt="""
Service Type:
    [1] IP Transit
    [2] MPLS
    [3] SD-WAN
    [4] Cross Connect
""",
    type=click.Choice(("1", "2", "3", "4")),
    required=True,
    help="Customer ID Number from CRM",
)
def get_info(customer_id, search_state, service_type):
    """
    Parses input data, passes to child functions, prints generated
    circuit ID
    """
    service_country = match_country_id("usa")
    service_state = match_state(search_state)
    id_number = random_id()
    circuit_loc_id = "".join([service_country, service_state[1], service_state[0]])
    circuit_id = ".".join([service_type, circuit_loc_id, str(customer_id), id_number])
    click.echo(
        click.style("\nCircuit ID: ", fg="black")
        + click.style(circuit_id + "\n", fg="cyan", bold=True)
    )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    get_info()
