#!/bin/bash
# Send a POST request with json file
curl -s -H "Content-Type: application/json" -X POST "$1" --data @"$2"
