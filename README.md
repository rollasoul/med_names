# med_names

This is a messy patched bunch of scripts that when put in the right place help running a torch-rnn on a remote server.
The torch-rnn is trained on 20 000 first names (only some 4000 steps to keep the output rough) and generates new names.
The client can be anything running python 2 and processing 3 (used a Raspberry Pi running Raspian) with a light sensor 
attached (used the ldr light sensor) - this triggers the first script and sends a request via sockets tp server,
torch-rnn generates some 1000 names, sends the list to client, client starts running a processing script and displays a flickering name.
It as well starts omxplayer playing back the waves.mp3 file (used a mini-speaker plugged into the audio port of the raspberry pi, 
bluetooth was too buggy). 

prerequisites:

- remote server (minimum specs 8gb ram)
- local client (e.g. raspberry pi) with python 2 and processing 3 installed

installation (server side):

- install docker on remote server
  sudo apt-get install docker.io
  sudo service docker start
  
- pull torch-rnn image with trained model from dockerhub
  sudo docker pull rollasoul/med_names

- start docker image / start docker container
  sudo docker run -it -p 12345:12345 rollasoul/med_names

- start python script to make server listen on port 12345
  python server_script.py
  
installation (client side)

- edit python script to change IP address (change line 11 "server address" to the one of your server)
  vi client_script.py

- run python script
  python med_names.py
  
... after covering the light sensor the client sends reuqest, on the server terminal you will see connection, ignore error about connection lost on client, it's fine. 
The python script will run a processing script and display the name on the screen - when the light sensor is covered "wait/read/write" will appear and the server called again.
  
  
