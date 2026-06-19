# GME Web API
## Simple Interface to use the GME Web Api programmatically

As the GME does not provide a public API to access data, I've made this library to allow the use of the web facing API used by the site to retrieve the values for various energy prices.

It may be subject to changes and the mechanism used for auth by the site could change anytime.


For now this has the package "requests" as the only dependency, this could be removed by using the built-in urllib3 module, but it's much more cumbersome to use, so that's it, if you don't like it, contributions are welcome!

Usage is pretty basic.\
import the package, initialize the api, get prices

everything apart the dates are type checked and enumerated trough classes so just check the source to get the options for the parameters, default to today pun with 15m prices.

it should be a package on pypi but i had no time for that yet, so you'll need to use this as a repo dependency if you want to use it programmatically.
---
```
import gmewebapi
#or
#from src import gmewebapi 
#if using locally from venv


gme = gmewebapi.GME()
gme.initialize()
gme.getPrice(20260620, 20260621, Granularita, Mercato, Zona, Tipologia)
```
