#!/bin/bash
#URL as an argument, sends a GET request to the URL, and displays the body
curl -sLH "X-School-User-Id: 98" "$1"
