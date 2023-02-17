 <img src="https://valueguard.se/static/media/valueguardlogo_black.f3a4c174.png" width="200">

# Valueguard Python Client


## Index

- [Introduction](#introduction)
  - [Description](#description)
  - [Installing](#installing)
- [Usage](#usage)
- [Community](#community)
  - [Support](#support)
  - [Contributing](#contributing)
- [Copyright](#copyright)


# Introduction

## Description

**Valueguard Python Client** is the official client used to interact with the new **Valueguards API**

Valueguard is a Swedish company that provides real estate valuation and analysis services for the housing market. The company was founded in 2007. Our primary service is to provide independent home valuations and analyses to banks, brokers and other companies that need reliable and accurate property information. Our services are based on various data sources, including historical transaction data, information about the property's location and condition, and other market data.

In addition to price statistics and valuations, Valueguard provides various other services, such as a complete registry of all homes in Sweden, called the Residential Registry. We have a team of experienced analysts who work to provide high-quality services to our clients.
We are proud to have a strong reputation in the Swedish real estate industry and are considered one of the country's leading providers of housing statistics.

## Installing

Install by pip

```
pip3 install git+https://github.com/Valueguard-Index-Sweden/valueguard-python-client#egg=valueguard
```

or

```
pip3 install valueguard
```


# Usage

- For **python client** documentation see [wiki-page](https://github.com/Valueguard-Index-Sweden/valueguard-python-client/wiki)
- For the **core Valueguard API** documentation, see the [api documentation](https://api.valueguard.se/swagger-ui.html).

```python
import valueguard

# Create object
vgClient = valueguard.Client()

# Generate a access token
vgClient.authenticate(<username>,<password>)

# Use wished function
print(vgClient.residential_registry(offset=0, limit=800, search_criteria={
                                                            "construction_year_min": 2018,
                                                            "construction_year_max": 2019
                                                            }))
```

# Community


## Support
Bugs, questions, and other issues can be directed to the project's [issues page](https://github.com/Valueguard-Index-Sweden/valueguard-python-client/issues) on GitHub, or emailed to [info@valueguard.se](mailto:info@valueguard.se).

## Contributing
Contributions are welcome in the form of code, bug fixes, or testing feedback. For more on how to contribute to Valueguard-python-client, see the [code of conduct](docs/CODE_OF_CONDUCT.md) and [contributing guidelines](docs/CONTRIBUTING.md).


# Copyright
MIT License

Copyright (c) 2020 Valueguard (info@valueguard.se)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
