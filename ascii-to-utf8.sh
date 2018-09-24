#!/bin/bash

iconv -t utf-16 $1 | iconv -f utf-16be -t utf-8 > ascii-to-utf8.tmp
rm $1
mv ascii-to-utf8.tmp $1
