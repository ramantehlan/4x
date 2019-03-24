# 4X

A cheap satellite weather data receiver, with GPS.

## Problem

``` yml
Fishing done by 14.5 million people.
And around 60 million in world.

They rely on smartphones and the internet, or the radio.
But most of the them still doesn't have ways to get weather forcast.
```

## Solution

``` yml
A cheap satellite weather data receiver, with GPS. (Keeping it under RS 4000)
- It don't need internet to work.
- It is far more cheap.
- It featch the real time data, directly from the satellite.
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

## How it works

``` yml
[STEP 1]: Read the weather and Navigation data from different satellites.
          - We will use the satellite broadcasting frequency.
            Indian Regional Navigation Satellite System (IRNSS) : 1176.45 MHz
            The National Oceanic and Atmospheric Administration (NOAA): 162.550 MHz
[STEP 2]: Process the collected data.
        - Decord `.wav` or `.dat` files.
        - Parse it into `JSON` format.
        - Send the `JSON` data to mongoDB.
[STEP 3]: Display it on the screen.
        - Use `elastic search` to fetch data.
        - Publish data on `kibana` dashboard.
```

## Examples/Demo

```
Under construction
```

## Future

``` yml
- We can use the satellite data ( mainly GPS data) to figure out the country water borders and can notify 
the fishermen about when they are close to crossing the water borders to avoid the legal consequesnces 
thereupon.

- The data from satellite ( mainly Color & Temperature Data ) can help the fishermen to know the spots
where they must avoid fishing as many endangered species exist in those spots.

- Satellite Data can help the fishermen know of the algal blooms & help them plan accordingly .
```

## Team

- Raman Tehlan `SDR`
- rajudev `IOT`
- Gaurav `Server`
- Ayon roy `Server`
