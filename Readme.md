# Technical Interview - Backend Test
## Requirements
Design a REST API endpoint that provides auto-complete suggestion for large
cities.
- The endpoint is exposed at /suggestions
- The partial or complete search term is passed as a query string parameter q
- The caller’s location can optionally be supplied via query string parameters latitude and longitude to improve relative scores.
- The endpoint returns a JSON response with an array of scored suggested matches
    - The suggestions are sorted by descending score
    - Each suggestion has longitude and latitude
    - Each suggestion has a name which can be used to differentiate between two locations
    - Each suggestion has a score between 0 and 1

## Rules
- The preferred programming language for this assessment is python and Django framework.
- End result should be deployed on a public cloud(Heroku, AWS etc. all have free tiers you can use).
- Create a repository and push your codes there and share the link to the github repository in your submission.
- Provide a swagger documentation to make the endpoint available for testing.

## Solution and Output
`.txt` over `db`
