
# Installation 
```
pip install -r requirements.txt
```

# Tutorial
https://www.edureka.co/blog/python-xml-parser-tutorial/

# Appendix: XPath Structure

## Activities
`/Activities/Activity[@Sport="Running"]/Id`
A timestamp serving as an Id for the activity.

`/Activities/Activity[@Sport="Running"]/Lap`
Each Lap is enclosed in its own tag.

`/Activities/Activity[@Sport="Running"]/Creator`
The device which recorded the activity.

## Laps

`/Activities/Activity[@Sport="Running"]/Lap/...`
A couple of summary fields like time, distance, average HR etc.

`/Activities/Activity[@Sport="Running"]/Lap/Extension`
A couple of extension summary fields like speed, cadence, watts

`/Activities/Activity[@Sport="Running"]/Lap/Track/Trackpoint`
A trackpoint every second with time, distance, HR
For outdoor activities a position and altitude meters are given

`/Activities/Activity[@Sport="Running"]/Lap/Track/Trackpoint/Extension`
A trackpoint extension with speed, cadence, watts





