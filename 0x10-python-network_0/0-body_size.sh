#!/bin/bash
# Use curl to get the content-length of the header
# Get the URL from the argument
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
