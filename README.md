# Simple Interface to use the GME Web Api programmatically

As the GME does not provide a public API to access data, instead you need to compile and send documents just to get the daily energy price, I've made this library to allow the use of the web facing API used by the site to retrieve the values for various energy prices.

It may be subject to changes and the mechanism used for auth by the site could change anytime, so this is not really "stable".

But, at the same time this is going in the direction of being able to actually use the official API with the authentication provided by the GME, hopefully they release a bit the required legal tasks needed to get it.

For now this has the package "requests" as the only dependency, this could be removed by using the built-in urllib3 module, but it's much more cumbersome to use, so that's it, if you don't like it, contributions are welcome!

Usage is pretty basic.\
import the package, initialize the api, get prices

Classes and functions all have docstrings, read them, official docs will come later on.

---

import gmewebapi

gme = gmewebapi.GME()
gme.initialize()
gme.getPrice(Inizio, Fine, Granularita, Mercato, Zona, Tipologia)
