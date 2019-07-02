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

## Installation

```console
$ pip install git+https://github.com/checktheroads/generate_circuit_id.git
```

## Usage

```console
$ generate-circuit-id
  CRM ID: 12345
  US State: hi

  Service Type:
      [1] IP Transit
      [2] MPLS
      [3] SD-WAN
      [4] Cross Connect
  : 3

 Circuit ID: 3.84048.12345.5821
```

Options can also be passed as arguements:

```console
$ generate-circuit-id --help
Usage: generate-circuit-id [OPTIONS]

  Parses input data, passes to child functions, prints generated circuit ID

Options:
  -c, --customer-id INTEGER  Customer ID Number from CRM  [required]
  -s, --state TEXT           US State Where Service is Delivered  [required]
  -t, --type [1|2|3|4]       Customer ID Number from CRM  [required]
  --help                     Show this message and exit.
```

```console
$ generate-circuit-id -c 12345 -s Hawaii -t 3
Circuit ID: 3.84048.12345.5821
```
# License
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>
