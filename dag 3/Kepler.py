import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz
from astropy.wcs import WCS

file = fits.open('data2.fits')

#file.info()

data = file[1].data

time_data = data.field('TIME')
#print('TIME')
#print(time_data)

flux = data.field('PDCSAP_FLUX')
#print('FLUX') 
#print(flux)

p=34/4
period = (time_data % p)/p

plt.clf()
plt.plot(period,flux,'.')
plt.show()