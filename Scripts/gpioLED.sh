#!/bin/bash
gpio mode 3 out
gpio mode 0 out
for i in {1..10}
do
gpio write 0 1
gpio write 3 0
sleep 1
gpio write 0 0
gpio write 3 1
sleep 1
done
