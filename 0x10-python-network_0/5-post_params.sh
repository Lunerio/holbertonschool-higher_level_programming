#!/bin/bash
# Send a POST request to set variables
curl -s -X POST -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
