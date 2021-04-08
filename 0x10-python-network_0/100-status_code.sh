#!/bin/bash
# Get the http_code from a request
curl -s -w '%{http_code}' "$1" -o /dev/null
