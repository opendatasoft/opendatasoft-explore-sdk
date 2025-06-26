#!/bin/sh

# Build the async sdk
sh ./generators/python-async/generate.sh

# Build the sync sdk
sh ./generators/python/generate.sh
