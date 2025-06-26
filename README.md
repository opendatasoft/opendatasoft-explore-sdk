# Opendatasoft Explore API SDK

This repository contains 2 versions of the same SDK:
* a sync version using `urllib3`
* an async version using `aoihttp`

## Installation

Refers to the README.md of the desired version
* [sync](./python/README.md)
* [async](./python-async/README.md)

## Development

Requirements:
* a running docker engine

First, update both openapi specifications ([`./generators/python/openapi/platform@v2.1.yaml`](./generators/python/openapi/platform@v2.1.yaml) or [`./generators/python-async/openapi/platform@v2.1.yaml`](./generators/python-async/openapi/platform@v2.1.yaml)).

Finally, run `./generate.sh`. It will run sequantially both `generate.sh` scripts of both SDK versions.