#!/bin/bash

function cutearp(){
    arp -n | awk '{if($1 ~ "[0-9]+.") print $5 " " $1 " " $3}'
}

function arpdiff(){
    diff arp.1 arp.2 | grep "[[:digit:]]\." | cut -d\  -f 3- | sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ -> /g'
}

cutearp > arp.1

while true
do
    sleep 3
    cutearp > arp.2
    nbdiff=$(diff arp.1 arp.2 | wc -l)
    if [ $nbdiff -gt 2 ] 
    then
        logger Aleteration de la table arp
        logger "$(arpdiff)"
        cutearp > arp.1
    fi
done
