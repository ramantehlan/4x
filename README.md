# 4x

A **Reliable**, **Portable** and **Cheap** satellite weather data receiver, which **doesn't require internet** to work.

This project was created in March-2019, during [HackBMU-2019](https://hackbmu.com/).

# Index

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Usage](#usage)
  - [Installation](#installation)
- [File Structure](#file-structure)
- [Contribution](#contribution)
- [Resources](#resources)
- [Gallery](#gallery)
- [Credit](#credit)
- [License](#license)

## Problem Statement

``` yml
14.5 million fishermen and sailors rely on smartphones and the internet, or the radio.
But most of them still don't have ways to get the weather forecast.

Expensive and centralized weather detection systems, on which millions of people depend.
```

## Solution


``` yml
A cheap satellite weather data receiver, with GPS. (Keeping it under RS 4000)
- It doesn't need the internet to work.
- It is far cheaper.
- It fetches the real-time data, directly from the satellite.
- It can be installed easily on the boats.


[Setup Cost]:
- 820T2 & SDR Dongle
  1pc: ₹750
- Orange Pi Zero 256MB  
  1pc: ₹990
- Screen, Battery, bulbs etc
  1pc: ~₹500
- Case
  1pc: ~₹150

Total: ₹2390
```

#### Other Implimentations

``` yml
- We can use the satellite data ( mainly GPS data) to figure out the country water borders and can notify
the fishermen about when they are close to crossing the water borders to avoid the legal consequences
thereupon.

- The data from satellite ( mainly Color & Temperature Data ) can help the fishermen to know the spots
where they must avoid fishing as many endangered species exist in those spots.

- Satellite Data can help the fishermen know of the algal blooms & help them plan accordingly.
```

## Usage

#### Installation

To use this project, perform the following steps in Raspberry Pi:

1. Clone this project. `$ git clone https://github.com/ramantehlan/4x/`
2. Make the install script executable. `$ chmod +x ./install` 
3. Install the script. `$ ./install` 

Once you have installed all the dependencies, you should plug in your SDR device and now we can run 4x. 

1. Start the server. `$ python3 ./server/server.py`.
2. Start the decoder. `$ ./decoder/build/4x-ARCHITECTURE`. 

After this, you can find server running on `http://127.0.0.1:2486/`. 

## File Structure

```console
.
├── README.md
├── install
├── .gitignore
├── decoder
│   ├── build
│   │   ├── 4x-armv7l
│   │   └── 4x-x86_64
│   ├── command.go
│   ├── e.go
│   └── main.go
├── build
│   ├── 4x-armv7l
│   └── 4x-x86_64
├── pi-infra-setup
│   └── docker-compose.yml
└── server
    ├── server.py
    ├── static/...
    └── templates/...
```

No | File/Folder Name | Details
---|------------------|--------
 1 | server | Server to display the decoded images on the dashboard.
 2 | server/server.py | Main file to start the server.
 3 | pi-infra-setup | Docker Compose for Raspberry Pi. 
 4 | decoder | It is the program to fetch and decode weather images.
 5 | decoder/build | This is to store the latest binary build of decoder for different architectures. 

## Contribution

Feel free to add your own features or improve any current feature, any kind of contribution is appreciated!

## Resources

- [SDR-Radio](https://www.sdr-radio.com/)
- [SDR-Wiki](https://en.wikipedia.org/wiki/Software-defined_radio)
- [Raspberry Pi](https://www.raspberrypi.org/)

## Gallery

![Img](https://raw.githubusercontent.com/ramantehlan/4x/master/server/static/images/ss.png)

## Credit

- Raman Tehlan
- Rajudev
- Gaurav
- Ayon Roy

## License

GNU General Public License v3.0
