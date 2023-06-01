# Technical Interview - Backend Test
## Requirements
Design a REST API endpoint that provides auto-complete suggestion for large
cities.
- [x] The endpoint is exposed at /suggestions
- [x] The partial or complete search term is passed as a query string parameter q
- [x] The caller’s location can optionally be supplied via query string parameters latitude and longitude to improve relative scores.
- [x] The endpoint returns a JSON response with an array of scored suggested matches
    - [x] The suggestions are sorted by descending score
    - [x] Each suggestion has longitude and latitude
    - [x] Each suggestion has a name which can be used to differentiate between two locations
    - [x] Each suggestion has a score between 0 and 1

## Rules
- [x] The preferred programming language for this assessment is python and Django framework.
- [x] End result should be deployed on a public cloud(Heroku, AWS etc. all have free tiers you can use).
- [x] Create a repository and push your codes there and share the link to the github repository in your submission.
- [x] Provide a swagger documentation to make the endpoint available for testing.

## Solution and Output
### Solution
I got the data from [Geonames](http://download.geonames.org/export/dump/readme.txt) and I downloaded two of the data files, `cities5000.zip` & `admin1CodesASCII.txt`.
- `cities5000.zip` contained the city information needed for this api expcept the other names that diffrentiates each city.
- `admin1CodesASCII.txt` contained the missing piece from `cities5000.zip`

I decided not to create my own database and populate it with this data because we're not performing any complex operations that a file can't handle and in a real scenario, it'll be more expensive to query the database several millions of times to get information that can be as well be accessed via file IO.

**Suggestion Score** - Implementing the suggestion scoring system was one of the challenges in developing this API. The `relevanceScore` function, which utilizes the `fuzzywuzzy` module, was straightforward to implement and provided satisfactory results. However, calculating the `proximityScore` posed some difficulties. Initially, I employed the Pythagorean theorem to calculate the distance between two points, and then used the hypotenuse to determine the proximity score. To avoid potential zero division errors, I added 1 to the denominator. Finally, I calculated the average of the relevance and proximity scores.

Upon further evaluation, I found that this solution was not optimal for accurately measuring proximity. In order to improve the accuracy of the proximity score calculation, I researched alternative methods and discovered the `geoPy` library. By utilizing `geoPy`, I obtained significantly smaller proximity score values compared to the initial solution.

To refine the scoring system, I decided to assign different weights to the relevance and proximity scores. Instead of treating them equally as in the case of the average, I assigned a weight of 7.5 to the `relevanceScore` and 2.5 to the `proximityScore`. This adjustment allows for a more balanced and meaningful overall suggestion score.

By incorporating these improvements to the scoring mechanism, the API provides more accurate and relevant suggestions for large cities, taking into account both their relevance to the search term and their proximity to the caller's location.

### Output
> Query Match
```
GET /suggestions?q=Londo&latitude=43.70011&longitude=-79.4163
```
```json
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "suggestions": [
        {
            "name": "London, Ontario, CA",
            "latitude": 42.98339,
            "longitude": -81.23304,
            "score": 0.77
        },
        {
            "name": "London, Ohio, US",
            "latitude": 39.88645,
            "longitude": -83.44825,
            "score": 0.72
        },
        {
            "name": "London, Kentucky, US",
            "latitude": 37.12898,
            "longitude": -84.08326,
            "score": 0.71
        },
        {
            "name": "London, England, GB",
            "latitude": 51.50853,
            "longitude": -0.12574,
            "score": 0.69
        },
        {
            "name": "New London, Connecticut, US",
            "latitude": 41.35565,
            "longitude": -72.09952,
            "score": 0.53
        },
        {
            "name": "New London, Wisconsin, US",
            "latitude": 44.39276,
            "longitude": -88.73983,
            "score": 0.53
        },
        {
            "name": "Londontowne, Maryland, US",
            "latitude": 38.93345,
            "longitude": -76.54941,
            "score": 0.5
        },
        {
            "name": "Londonderry, New Hampshire, US",
            "latitude": 42.86509,
            "longitude": -71.37395,
            "score": 0.49
        },
        {
            "name": "East London, Eastern Cape, ZA",
            "latitude": -33.01529,
            "longitude": 27.91162,
            "score": 0.47
        },
        {
            "name": "City of London, England, GB",
            "latitude": 51.51279,
            "longitude": -0.09184,
            "score": 0.4
        },
        {
            "name": "West End of London, England, GB",
            "latitude": 51.51414,
            "longitude": -0.1551,
            "score": 0.33
        },
        {
            "name": "Londonderry County Borough, Northern Ireland, GB",
            "latitude": 54.99721,
            "longitude": -7.30917,
            "score": 0.24
        }
    ]
}
```
> No Match
```
GET /suggestions?q=SomeRandomCityInTheMiddleOfNowhere
```
```json
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "suggestions": []
}
```

## SetUp & Installation

```shell
# open the project folder in terminal
# create a virtual environmet
$ py -m venv venv
# activate the virtual environment
$ venv/scripts/activate
# install project requirements
$ pip install -r requirements.txt

# Run the program
$ python manage.py runserver

# Starting development server at http://127.0.0.1:8000/
# swagger at /swagger
# redoc at /redoc
# suggestions at /suggestions
