# gmewebapi

A clean and lightweight Python wrapper for interacting with the GME Web API.

[![PyPI version](https://img.shields.io/pypi/v/gmewebapi.svg)](https://pypi.org/project/gmewebapi/)
[![Build Status](https://github.com/moddroid94/gmewebapi/actions/workflows/python-publish.yml/badge.svg)](https://github.com/moddroid94/gmewebapi/actions)
[![GitHub stars](https://img.shields.io/github/stars/moddroid94/gmewebapi.svg)](https://github.com/moddroid94/gmewebapi/stargazers)
[![License](https://img.shields.io/github/license/moddroid94/gmewebapi.svg)](https://github.com/moddroid94/gmewebapi/blob/master/LICENSE)

---

## Features

- **Asynchronous Support**: Built to work seamlessly with async Python applications.
- **Simple Interface**: Minimizes boilerplate to make API requests straightforward.
- **Lightweight**: Minimal dependencies to keep your environment clean.
- **Type-Safe**: Provides basic typing support for improved developer experience.

## Installation

Install the package via `pip`:

```bash
pip install gmewebapi
```
Or using uv / poetry:
```
uv add gmewebapi
```
## Quick Start

Below is a simple example showing how to initialize the client and fetch data:
```
import asyncio
import gmewebapi

async def main():
    # Initialize the client (configure with your credentials as needed)
    async with gmewebapi.GME() as gme:
        #get token, return true if ok
        if gme.initialize():

        #get prices data
        prices = gme.getPrice(20260620, 20260621, Granularita, Mercato, Zona, Tipologia)
        print(prices)

if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing

Contributions are welcome. If you find a bug or have a feature request, feel
free to open an issue or submit a pull request:

1.  Fork the repository.
2.  Create a feature branch (git checkout -b feature/amazing-feature).
3.  Commit your changes (git commit -m 'Add some amazing feature').
4.  Push to the branch (git push origin feature/amazing-feature).
5.  Open a Pull Request.

License

Distributed under the AGPL3 License. See LICENSE.MD for more information.
