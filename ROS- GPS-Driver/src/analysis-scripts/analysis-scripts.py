import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import utm

gpswalking = pd.read_csv('eece5554/LAB1/src/data/walking_data_2022-09-23-17-12-39/gps.csv')
gpsstatic = pd.read_csv('eece5554/LAB1/src/data/standard_test_2022-09-24-21-19-32/gps.csv')

def latlon_to_utm(lat, lon):

  utm_e, utm_n, zone, letter = utm.from_latlon(lat, lon)

  return utm_e, utm_n, zone, letter

utm_e, utm_n, zone, letter = latlon_to_utm(gpsstatic['latitude'].to_numpy(), gpsstatic['longitude'].to_numpy())
gpsstatic['UTM_northing_correct'] = utm_n
gpsstatic['UTM_easting_correct'] = utm_e


utm_e1, utm_n1, zone1, letter1 = latlon_to_utm(gpswalking['latitude'].to_numpy(), gpswalking['longitude'].to_numpy())
gpswalking['UTM_northing_correct'] = utm_n1
gpswalking['UTM_easting_correct'] = utm_e1

gpsstatic['UTM_northing_standard'] = gpsstatic['UTM_northing_correct'] - gpsstatic['UTM_northing_correct'].min()
gpsstatic['UTM_easting_standard'] = gpsstatic['UTM_easting_correct'] - gpsstatic['UTM_easting_correct'].min()

gpswalking['UTM_northing_standard'] = gpswalking['UTM_northing_correct'] - gpswalking['UTM_northing_correct'].min()
gpswalking['UTM_easting_standard'] = gpswalking['UTM_easting_correct'] - gpswalking['UTM_easting_correct'].min()

gpsstatic[['UTM_northing_standard', 'UTM_easting_standard']].plot()

gpswalking[['latitude', 'longitude']].plot.scatter(x="latitude", y="longitude")

gpsstatic[['UTM_northing_standard', 'UTM_easting_standard']].plot.scatter(x='UTM_northing_standard', y='UTM_easting_standard')

gpswalking[['UTM_northing_standard', 'UTM_easting_standard']].plot.scatter(x='UTM_northing_standard', y='UTM_easting_standard')
 
plt.show()
