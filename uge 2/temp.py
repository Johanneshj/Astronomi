import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import astropy.visualization as viz
from astropy.wcs import WCS

file = fits.open('mf200096_ast.fit')

centerX = 700
centerY = 564

data = file[0].data

plt.clf()
#plt.xlim(centerX-100,centerX+100)
#plt.ylim(centerY-100,centerY+100)
thisCircle = plt.Circle((centerX, centerY), 20, color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)
plt.imshow(data,cmap='gray',clim=(np.percentile(data,1),np.percentile(data,99)),origin= 'lower')
plt.show()