# 2025-fide

International Chess Federation (FIDE) ratings


## Content

* **data/** the data in [tsv](https://en.wikipedia.org/wiki/Tab-separated_values).
	* **players.tsv**   players details
	* **ratings.tsv**   player's ratings (1 to many)
	* **titles.tsv**    player's titles (1 to many)
	* **countries.tsv** country codes used by FIDE
	* **iso3.tsv**      country codes used by ISO and regions
* **viz/** sample visualisations
* **vendor/** vendorized d3 v7.8.5 library

## Data structure

The attributes present in the **players** table are:

* **id**          a unique id for character (465877 values)
* **name**        player's name
* **fed**         player's chess federation (FIDE country code)
* **sex**         {'M', 'F'}
* **birthyear** 
* **max_rating**  maximum [ELO](https://en.wikipedia.org/wiki/Elo_rating_system) rating achieved
* **month**       month of achievement for max_rating ('%Y-%m' time format)

The attributes present in the **ratings** (1 to many) table are:

* **id**      reference to a player
* **month**   month fot the rating ('%Y-%m' time format)
* **rating**  ELO rating for that month
* **games**   number of game played that month

The attributes present in the **titles** (1 to many) table are:

* **id**      reference to a player
* **month**   month fot the rating ('%Y-%m' time format)
* **title**   [FIDE title](https://en.wikipedia.org/wiki/FIDE_titles) acquired that month

The attributes present in the **countries** table are:

* **#country**  name of the country in english
* **ioc**       FIDE country code (can be matched against the player's fed attribute)
* **alpha3**    the [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code (can be used as a key for lookup into the iso3 dataset)

The attributes present in the **iso3** table are:

* **#alpha3**   the [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code (156 values)
* **country**   name of the country in english
* **subregion** world subregion (~sub continent)
* **region**    world region (~continent)


## Sample visualizations

* **viz/0-top20.html** a HTML list of the top 20 players [D3.js](https://d3js.org/)
* more to come