#!/bin/bash
# Get the allowed methods in a server
curl -s "$1" --head | grep 'Allow:' | cut -d":" -f2 | awk '{$1=$1;print}'
