#!/usr/bin/env python

from ftplib import FTP
import os

# Set directory
ftppath = 'ftp.cdc.noaa.gov'
ftpdir = '/Datasets/udel.airt.precip/'
destinationdir = 'C:/hwacallo/netCDF/'

ftp=FTP(ftppath,)
ftp.login()
ftp.cwd(ftpdir)

# Local variables
filelist = ['air.mon.mean.v301.nc', 'precip.mon.total.v301.nc']

# Download files
for filename in filelist:
        print 'Downloading file from ' + ftppath + ftpdir + filename
        file = open(destinationdir + filename, 'wb')
        ftp.retrbinary('RETR %s' % filename, file.write)
ftp.quit()

print "FIN"
