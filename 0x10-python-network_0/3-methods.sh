#!/bin/bash
#Write a Bash script that takes in a URL and displays all HTTP methods the server will accept
w=$(curl -sIX OPTIONS "$1" | grep "Allow"); echo "$w"
