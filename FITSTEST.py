from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math

hdulist=fits.open('o4201193.10.fts')

imdata = hdulist[0].data

xcenter = 181
ycenter = 268

xcenterV = 214
ycenterV = 239

xcenterB = 215
ycenterB = 314


radius=8
photCollector=np.array([])
for ii in range(xcenter-radius, xcenter+radius):
    for jj in range(ycenter-radius,ycenter+radius):
        distance = np.sqrt((ii-xcenter)**2 +
            (jj-ycenter)**2 )
        if distance < radius:
            photCollector = np.append(photCollector, imdata[jj][ii])
C = np.sum(photCollector)
A = len(photCollector)

radiusV=8
photCollectorV=np.array([])
for ii in range(xcenterV-radiusV, xcenterV+radiusV):
    for jj in range(ycenterV-radiusV,ycenterV+radiusV):
        distance = np.sqrt((ii-xcenterV)**2 + (jj-ycenterV)**2 )
        if distance < radiusV:
            photCollectorV= np.append(photCollectorV, imdata[jj][ii])
CV = np.sum(photCollectorV)
AV = len(photCollectorV)

radiusB=18
photCollectorB=np.array([])
for ii in range(xcenterB-radiusB, xcenterB+radiusB):
    for jj in range(xcenterB-radiusB,ycenterB+radiusB):
        distance = np.sqrt((ii-xcenterB)**2 +
            (jj-ycenterB)**2 )
    if distance < radiusB:
        photCollectorB = np.append(photCollectorB,
            imdata[jj][ii])
CB = np.sum(photCollectorB)
AB = len(photCollectorB)

# Defining count/pixel for backkground
#N_sky = CB/AB

# Defining total area of object
#n_pix = A

# Defining count for object
#N_meas = C

# Subtracting background from object
#N_obj = N_meas - (N_sky*n_pix)

# Calculating S/N
g = 1.8
#SN = (g*N_obj)/(np.sqrt(g*N_obj+n_pix*g*N_sky+n_pix*5.1**2))
#print('SN=')
#print(SN)

# Maximizing SN
SN_vals = []
for q in range(1, 21):
    radius = q
    print(q)

    photCollector = np.array([])
    for ii in range(xcenter - radius, xcenter + radius):
        for jj in range(ycenter - radius, ycenter + radius):
            distance = np.sqrt((ii - xcenter) ** 2 +
                               (jj - ycenter) ** 2)
            if distance < radius:
                photCollector = np.append(photCollector, imdata[jj][ii])
    C = np.sum(photCollector)
    A = len(photCollector)

    # Defining count/pixel for background
    N_sky = CB / AB

    # Defining total area of object
    n_pix = A

    # Defining count for object
    N_meas = C

    # Subtracting background from object
    N_obj = N_meas - (N_sky * n_pix)

    SN = (g*N_obj)/(np.sqrt(g*N_obj+n_pix*g*N_sky+n_pix*5.1**2))
    SN_vals.append(SN)

print(SN_vals)

plt.clf()
rs = list(range(1, 21))
print(rs)
plt.plot(rs,SN_vals)
plt.show()





#ls1=C3-((C1-C2)/(A1-A2))*A3
#lv=CV3-((CV1-CV2)/(AV1-AV2))*AV3
#print('ls1=')
#print(ls1)
#print('lv=')
#print(lv)

#print('delta_m')
#delta_m = -2.5*math.log10(lv/ls1)
#print(delta_m)

#N_obj =
#N_sky = CB/AB
#n_pix = A1
#N_objV = CV3-(CV1-CV2)
#N_skyV = (CV1-CV2)/(AV1-AV2)
#n_pixV = AV1




#print('SNs1=')
#print(SNs1)

#SNV = (g*N_objV)/(np.sqrt(g*N_objV+n_pixV*g*N_skyV+n_pixV*5.1**2))
#print('SNV=')
#print(SNV)

plt.clf()
plt.axes().set_aspect('equal')
plt.imshow(imdata,cmap='gray',clim=(np.percentile(imdata,1),np.percentile(imdata,98)))

thisCircle = plt.Circle((xcenter, ycenter), radius, color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)

thisCircle = plt.Circle((xcenterV, ycenterV), radiusV, color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)

thisCircle = plt.Circle((xcenterB, ycenterB), radiusB, color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)

plt.show()




# Pick another circle for background.