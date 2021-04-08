#!/bin/bash
# Get a response from the given argument
curl -s -X PUT 0.0.0.0:5000/catch_me -L -H "Origin: HolbertonSchool" -d "user_id=98"
