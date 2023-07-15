# Zanussi Water Heater

## Build ESPHome firmware

```yaml
substitutions:
  # main prefix for all entities
  name: "Boiler"
  # name of your node
  node_name: "zanussi-artendo-pro"
  # use "esp12e" for iot-uni-dongle, "esp8285" for coolrf-heatstick, or your own if you know it
  board: "esp12e"
  # time platform: "sntp" or "homeassistant"
  time_platform: "sntp"
  # SSID of your wifi
  wifi_ssid: "natali"
  # password of your wifi
  wifi_password: ""
  # password for fallback wifi hotspot
  wifi_ap_password: ""
  # version of ewh
  ewh_version: "2022.1.2"

# please do not change packeages order it is very important, just comment/uncomment
packages:
  # required package, do not comment
  ewh: github://creasoftua/esphome-ewh/ewh-pkg-ewh.yaml@$ewh_version

  ## optional package, uncomment next line to enable additional diagnostic clock sensor
  clock: github://creasoftua/esphome-ewh/ewh-pkg-clock.yaml@$ewh_version

  ## optional package, uncomment next line to enable additional diagnostic timer sensor
  # timer: github://creasoftua/esphome-ewh/ewh-pkg-timer.yaml@$ewh_version

  ## optional package, uncomment next line to enable standalone web ui
  # web: github://creasoftua/esphome-ewh/ewh-pkg-web.yaml@$ewh_version

  ## optional package, uncomment next line to enable experimental cloud support
  # cloud: github://creasoftua/esphome-ewh/ewh-pkg-cloud.yaml@$ewh_version

  # required package, do not comment
  core: github://creasoftua/esphome-ewh/ewh-pkg-core.yaml@$ewh_version
```
