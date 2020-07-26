# ultrasonic_pi
Used to show distance measured by ultrasonic using a max7219 matrix board.

# Usase
python ultrasonic.py

# Install required library
To use the provided library file luma.led_matrix library is to be installed. However offical support of the library for python 2.7 has been dropped. So it should be manually installed.
Follow following steps:

$ git clone https://github.com/rm-hull/max7219.git

$ cd max7219

$ sudo pip install -e 

Also to transfer the data through SPI, the raspberrypi SPI sould be enabled and spidev python library should also be installed as:

$ cd max7219

$ sudo apt-get install python-dev python-pip

$ sudo pip install spidev

$ sudo python setup.py install
