# COVID-19 API


> This is a fast (< 200ms) and basic API for tracking development of the new coronavirus (2019-nCoV). It's written in Python using 🍼 Flask and also contains historical data 📈. I've also programmed a skeduler on the app to refresh the data every 10 minutes.

## Endpoints

All requests must be made to the base url: ``https://covid19api.herokuapp.com/``. You can try it out in your browser to further inspect responses.

Getting confirmed cases, deaths, and recoveries:

```http
GET /
```
```json
{ "latest": { ... }, "confirmed": { ... }, "deaths": { ... }, "recovered": { ... } }
```

Getting just confirmed:

```http
GET /confirmed
```
```json
{ "latest": 418678, "locations": [ ... ] }
```

Getting just deaths:

```http
GET /deaths
```
```json
{ "latest": 18625, "locations": [ ... ] }
```

Getting just recovered:

```http
GET /recovered
```
```json
{ "latest": 35000, "locations": [ ... ] }
```

Getting just latest data:

```http
GET /latest
```
```json
{ "confirmed": 418678, "deaths": 18625, "recovered": 35000}
```

Getting update datetime:

```http
GET /updatedAt
```
```json
2020-03-27 12:00:12.067975
```

## Data

The data comes from the [2019 Novel Coronavirus (nCoV) Data Repository, provided
by JHU CCSE](https://github.com/CSSEGISandData/2019-nCoV). It is
programmatically retrieved, re-formatted and stored in the server for every 10 minutes.

## Prerequisites

You will need the following things properly installed on your computer.

* [Python 3](https://www.python.org/downloads/) (with pip)
* [Flask](https://pypi.org/project/Flask/)
* [Heroku](https://devcenter.heroku.com/articles/heroku-cli)

## Installation

* `git clone https://github.com/INGENIANCE/COVID-19-API`
* `cd COVID-19-API`
* `pip install -r requirements.txt`

## Running / Development

* `python app.py`
* Visit your app at [http://localhost:5000](http://localhost:5000).

### Deploying

* Create a Heroku account
* Create a Heroku application
* `heroku login`
* `git init`
* `heroku git:remote -a <AppName>`
* `git add .`
* `git commit -am "first commit"`
* `git push heroku master`

### Testing

* Visit your application webpage
* `https://<AppName>.herokuapp.com/`

## License

The data is available to the public strictly for educational and academic research purposes.
