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
A cheap satellite weather data receiver, with GPS. (Under RS 4000)
- It don't need internet to work.
- It is far more cheap.
- It featch the real time data, directly from the satellite.
- It can be installed easily on the boats.
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

```
Not yet decided
```

## Team

- Raman Tehlan `SDR`
- Raju Dev `IOT`
- Gourav `Dashboard`
- Ayon roy `Dashboard`
