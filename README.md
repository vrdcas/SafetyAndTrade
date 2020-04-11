# SafetyAndTrade
Our project consists of constructing a comprehensive dataset that contains detailed information about maritime routes used for seaborne trade. We build a dataset of routes used by cargo vessels with given geographic origins and destinations using AIS vessel tracking data. The decision of which route to take relies on many factors, most importantly, weather conditions and risk of pirate raids. Therefore, we also collect geocoded data on weather conditions, and we digitalize every report of the Commercial Crime Services (ICC) on events of piracy and armed robberies against ships around the world for the same period. Finally, it has been argued that the U.S. Navy plays an important role in protecting seaborne trade routes around the world. For this reason, we also collect geocoded locations of U.S. Naval fleets between July 2017 and today to account for this additional factor of safety. The data can then be used in two ways.
1) We can use it to estimate the magnitude of the costs associated with maritime piracy. These costs can be associated with deviations from optimal routes or decreases in the level of seaborne trade between any two ports. We can also measure the benefit provided by the U.S. Naval fleet in deterring maritime piracy in different regions of the world.
2) The data can also be used to provide real-time safety information about different routes for sailors. We could generate a live map that shows which areas are not safe, based on the occurrence of pirate attacks, U.S. fleets location and the current traffic of civilian ships. We believe that this could be valuable for sailors when deciding which route to take.


Datasets on: 
1 - routes used by cargo vessels with given geographic origins and destinations using AIS vessel tracking data
2- geocoded data on weather conditions
3- reports of the Commercial Crime Services (ICC) on events of piracy and armed robberies against ships around the world for the same period
4 - geocoded locations of U.S. Naval fleets between July 2017 and 2020

Codes:
- Python scraping code for U.S Navy fleet locations by date (with file of extracted images and dates: Navy_dates.csv)
