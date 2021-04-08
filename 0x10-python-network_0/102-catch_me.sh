#!/bin/bash
# Get a response from the given argument
curl -X PUT "$1" -L -H "Origin: HolbertonSchool" -d "user_id=98"
