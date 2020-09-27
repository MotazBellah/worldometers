# World Population

Scrap the worldometers website and return csv and excel file with country, year and population
- https://www.worldometers.info/world-population/population-by-country/

## Code style

- This project is written in python 3.
- Use Scrapy.

## Clone/Run app
````
# Clone repo
$ git clone https://github.com/MotazBellah/worldometers

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ cd worldmeters
$ scrapy crawl countries -o outputfile.csv -t csv

```
