

![alt tag] (https://github.com/rollasoul/med_names/blob/master/DSC_0257.jpg)


# med_names

This is a small, messy, patched bunch of scripts that when put in the right place together with a [docker] (https://www.docker.com/) image help running Justin Johnson's [torch-rnn] (https://github.com/jcjohnson/torch-rnn) on a remote server. It was used in an art installation (see pic above). The torch-rnn is already trained on 20 000 first names (only some 4000 steps to keep the output rough) and generates new names. The client can be anything running python 2 and processing 3 (used a Raspberry Pi running Raspian) with a light sensor attached (used the ldr light sensor) - this triggers the first script and sends a request via sockets tp server, torch-rnn generates some 1000 names, sends the list to client, client starts running a processing script and displays a flickering name. It as well starts omxplayer playing back the waves.mp3 file (used a mini-speaker plugged into the audio port of the raspberry pi, bluetooth was too buggy). 

(also check the [project-website] (http://ouiouioui.space/lab#/nom/) for video of installation and detailed setup of raspberry pi)

general prerequisites:

- remote server (minimum specs 8gb ram)
- local client (e.g. raspberry pi) with python 2 and processing 3 installed

# install and run server side


- install docker on remote server
  ```
  sudo apt-get install docker.io
  
  sudo service docker start
  ```
  
- pull torch-rnn image with trained model from dockerhub
  ```
  sudo docker pull rollasoul/med_names
  ```

- start docker image / start docker container
  ```
  sudo docker run -it -p 12345:12345 rollasoul/med_names
  ```

- start python script to make server listen on port 12345
  ```
  python server_script.py
  ```
  
# install and run client side

- edit python script to change IP address (change line 11 "server address" to the one of your server)
  
  ```
  vi client_script.py
  ```
- edit processing script to change directory of med_names1.txt file with the list of names to the location it will be           downloaded to from server (by default in the /home/pi/ folder)
  ```
  vi mednames.pde
  ```
- download the [waves-recording] (https://www.freesound.org/people/Corsica_S/sounds/197714/) from freesound.org (you have to sign-up for this), convert and rename it to waves.mp3

- run python script
  ```
  python med_names.py
  ```
  
... after covering the light sensor the client sends reuqest, on the server terminal you will see connection, ignore error about connection lost on client, it's fine. 
The python script will run a processing script and display the name on the screen - when the light sensor is covered "wait/read/write" will appear and the server called again.
  
  
