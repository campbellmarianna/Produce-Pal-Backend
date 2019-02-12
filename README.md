# Produce Pal

This app is a one-stop shop for farmers market.
**_Produce Pal_** is being created with Python, Swift and the official USDA National Farmers Market Directory API.

Official USDA National Farmers Market Directory API website:  https://search.ams.usda.gov/farmersmarkets/v1/svcdesc.html

Website: https://producepal.herokuapp.com/

## Running Locally
Make sure you have [Python](https://www.python.org/) >= 3 installed.

```sh
git clone https://github.com/campbellmarianna/Produce-Pal-Backend.git
cd produce-pal-backend
```

The app should now be running on [localhost:3000](http://localhost:3000/).

Users can see farmer's markets and more information on a single farmer's market.

```
Index - https://producepal.herokuapp.com/markets
Show - https://producepal.herokuapp.com/market/<string:name>
```

## Project Backend Team

Created by Eric Botcher and Marianna Campbell in Software Product Development(SPD) 1.3 at Make School

Eric's Github -  https://github.com/capt-alien
Marianna's Github - https://github.com/campbellmarianna


The Markets resource will have the following Schema*:
_id, M_name, Address, lat_long, day_time, session, website, venders

*Please note that these are just preliminary, if you have any ideas for fields we
should use for this please bring it up on the slack channel.
