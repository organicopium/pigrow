# PiGrow

### Motivation
Some plants, like the Indian Green Chillies that I have, require very delicate conditions in their seedling state. You need to continously monitor their temperature and humidity in order to get an Idea of how these environmental variables affect them. So, I decided to implement my own low-cost system that would let me keep an eye on these conditions.

### Function
This system reads Temperature and Relative Humidity every 30 seconds and saves it in a sqlite database locally. The project also provides a minimalistic web interface that let's you monitor the latest measurements. The system also broadcasts an RTSP live stream of the scene.

### Requirements

#### Software
  - **python** > 3.x
  - **virtualenv** (optional but recommended)
  - **pip**
  - **screen** utility to run detached terminals. (sudo apt install screen)

#### Hardware
  - Raspberry Pi
  - [DHT22 Sensor](https://www.amazon.it/gp/product/B07CM2VLBK/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
  - [Raspicam](https://www.amazon.it/gp/product/B073RCXGQS/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
 
### Setup
This system is supposed to be a Headless Plug n Play. You only need to configure it the very first time and afterwards it would run automatically whenever you plug in the power cord and connect it to the internet. So, it is recommended to disable DHCP and give your raspberry a static ip address that you would remember. This will save you a lot of hassle in the future.

  - Create a Python 3.7 Virtual Environment.
  - Install the required libraries via requirements.txt file provided by the project  ``` pip install -r requirements.txt ```
  - Open *pigrow/static/start_measuring.sh* and make sure that *${scpath}* is pointing to the location where your virtual environment's activation file is. For example ``` scpath="/home/pi/projects/pigrowenv/bin/activate" ```. While you are at it, verify whether all the other paths in this script are correct according to your file directory.
  - Open ~/.bashrc and the following lines. You would need to change these paths according to where you cloned the repository.

```
screen -dmS sh /home/pi/projects/pigrow/static/start_measuring.sh
cd /home/pi/projects/pigrow/static/
screen -dmS  raspcam ./campipeline.sh
```

### Test
- In oder to test the DHT22 reading you could open up any browser and type in the address bar ```http://<raspberry's ip>/dht/```
- If you want to see the live stream then you could use VLC player(or any other player capable of reproducing RTSP stream in .h264 format) and go to ```Media -> Open Network Stream``` and type the following link in the URL field ```rtsp://<raspberry's ip>:8554/stream```


### More to come
- Currently all the paths are ad-hoc for my personal setup, I am planning to make them all dynamic so the user would not have to deal with the manual configurations.
- I don't like how you need an additional VideoPlayer to view the stream. In the near future the video will be played on a webpage with some javascript based player.
- Currently you could only see the LATEST temperature and humidity and if you want to analyze the previous readings, you have to manually open the database file with some kind of viewer. I will be adding support on the web-page to see all the historical readings as well and maybe even plot some graphs to see the change in these variables.
- Addition of Relays or Smart Plugs so you could turn on/off the humidifier and lights form the web-page.

### In Action
![screenshot of the system in action](https://github.com/organicopium/pigrow/blob/main/example2.png?raw=true)
![picture of the physical setup](https://github.com/organicopium/pigrow/blob/main/setup2.jpg?raw=true)
