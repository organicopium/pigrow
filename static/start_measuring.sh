#!/bin/bash
export scpath="/home/pi/projects/pigrowenv/bin/activate"
source ${scpath}
python /home/pi/projects/pigrow/static/dht22Measure.py > /dev/null $
