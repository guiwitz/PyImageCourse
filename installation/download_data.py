import sys, os, zipfile
import urllib.request
import requests

#where_to_save = '../Data/'
where_to_save = 'Data/'

#create data directory
if not os.path.exists(where_to_save):
    os.makedirs(where_to_save)
    
#import Klee painting
url = 'https://img.myswitzerland.com/671846/407'  
urllib.request.urlretrieve(url, where_to_save+'Klee.jpg')

#import zebrafish embry
os.makedirs(where_to_save+'30567')
url = 'https://cildata.crbs.ucsd.edu/media/images/30567/30567.tif'  
urllib.request.urlretrieve(url, where_to_save+'30567/30567.tif')

#import scifio wtembryo
os.makedirs(where_to_save+'2chZT')
url = 'https://samples.scif.io/2chZT.zip'
urllib.request.urlretrieve(url, where_to_save+'2chZT.zip')
#unzip
with zipfile.ZipFile(where_to_save+'2chZT.zip', 'r') as zip_ref:
    zip_ref.extractall(where_to_save+'2chZT')
os.remove(where_to_save+'2chZT.zip')

#import landsat images
os.makedirs(where_to_save+'geography')
url = 'https://ndownloader.figshare.com/files/7677208'
urllib.request.urlretrieve(url, where_to_save+'geography.zip')
#unzip
with zipfile.ZipFile(where_to_save+'geography.zip', 'r') as zip_ref:
    zip_ref.extractall(where_to_save+'geography')
os.remove(where_to_save+'geography.zip')

#import BBBC007
url = 'https://data.broadinstitute.org/bbbc/BBBC007/BBBC007_v1_images.zip'
urllib.request.urlretrieve(url, where_to_save+'BBBC007_v1_images.zip')
#unzip
with zipfile.ZipFile(where_to_save+'BBBC007_v1_images.zip', 'r') as zip_ref:
    zip_ref.extractall(where_to_save)
os.remove(where_to_save+'BBBC007_v1_images.zip')

#import BBBC032
os.makedirs(where_to_save+'BBBC032_v1_dataset')
url = 'https://data.broadinstitute.org/bbbc/BBBC032/BBBC032_v1_dataset.zip'
urllib.request.urlretrieve(url, where_to_save+'BBBC032_v1_dataset.zip')
#unzip
with zipfile.ZipFile(where_to_save+'BBBC032_v1_dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(where_to_save+'BBBC032_v1_dataset')
os.remove(where_to_save+'BBBC032_v1_dataset.zip')

#import BBBC034
os.makedirs(where_to_save+'BBBC034_v1_dataset')
url = 'https://data.broadinstitute.org/bbbc/BBBC034/BBBC034_v1_dataset.zip'
urllib.request.urlretrieve(url, where_to_save+'BBBC034_v1_dataset.zip')
#unzip
with zipfile.ZipFile(where_to_save+'BBBC034_v1_dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(where_to_save+'BBBC034_v1_dataset')
os.remove(where_to_save+'BBBC034_v1_dataset.zip')

#import channels
os.makedirs(where_to_save+'channels')
url = 'https://drive.google.com/uc?id=1kNzXN_FkRflU4uNOpNfmpK8hUcJ1Dz6R'
urllib.request.urlretrieve(url, where_to_save+'channels/channels1.tif')
url = 'https://drive.google.com/uc?id=1OMBGdO3t_RvCIcmTLPX6zBfRiWt5KP3Z'
urllib.request.urlretrieve(url, where_to_save+'channels/channels2.tif')

#download heart
myfile = requests.get('https://zenodo.org/record/1211599/files/cxcr4aMO2_290112.lsm?download=1', allow_redirects=True)
open(where_to_save+'cxcr4aMO2_290112.lsm', 'wb').write(myfile.content)
