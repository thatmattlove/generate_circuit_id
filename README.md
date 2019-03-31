# `generate-circuit-id`
This insanely simple, unintentionally patriotic script generates a circuit ID based on input variables.

Circuit IDs are composed of the following variables:
- Service Type (IP Transit, MPLS, SD-WAN)
- Location Identifier
  - Combination of country (USA, in my case)
  - US Region ID (From [list](https://www.census.gov/geo/reference/gtc/gtc_census_divreg.html) from the US Census Bureau)
  - US Division ID (From the same list)
  - US State FIPS Code (From the same list)
- Customer ID
  - Should be something reusable that maps to the customer across all systems. In our case, the ConnectWise Company RecID
- Service ID
  - Randomly generated 4 digit number

This is pretty tailored to our environment and standards, but who knows, perhaps it would be useful to some other souls out there.

# Usage
## Install requirements
```console
# pip3 install -r requirements.txt
```
## Run
```console
# python3 generate_circuit_id.py
# CRM ID: 12345
# IP Transit [1], MPLS [2], SD-WAN [3]: 1
# Location (US State): Arizona
#
# Your circucit ID is:   1.84047.12345.7371
#
```

# License
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>
