## House Location Evaluation
### Introduction
I don't think Zillow or Redfin provides this yet, but I found this to be a neat feature. Usually, 
the website gives you a "walk score". Well, if you are living in suburb anyway, probably not really walkable
in the first place. And you have places you need to go: your office, your kid's school, your favorite restaurant
and the grocery store. You'll need a personal score for yourself to keep track. This gives you the option to
get the shortest path, to a collection of places you want. You can even group the destinations, if they are all
grocery stores, or McDonalds'.

### Usage
You'll want to install Google Maps <https://github.com/googlemaps/google-maps-services-python>. Run
`pip install -U googlemaps` to install it right away. 
I recommend using a venv if you are not shy of disk space.

You can either update `house_location.txt` or use command line directly with the address in args.
You'll want to update the dict: `frequent_places_departure_time` in `house_location_eval.py`.

```
python main.py
python main.py "6719 SE 5th St SE Renton, WA 98059"
```