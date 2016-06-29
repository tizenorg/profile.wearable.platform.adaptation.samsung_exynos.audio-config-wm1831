#!/bin/sh
PATH=/bin:/usr/bin:/sbin:/usr/sbin

filename=/root/largo_register.txt
if [ "$1" ]
then
largo_debug=$1/largo
mkdir -p ${largo_debug}
filename=${largo_debug}/largo_register.txt
fi
register=/sys/kernel/debug/regmap/spi1.0/registers
/usr/bin/head -701 $register >> $filename
