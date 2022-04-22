#!/bin/bash
# takes in a URL and displays HTTP methods server will ok
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
