#!/bin/bash
raspivid -o - -t 0 -n -w 640 -h 480 -vf -fps 24  | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264 --h264-fps=24
