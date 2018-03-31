# 气象数据读写及访问程序库
Provides data I/O functions for MICAPS, satellite,
weather radar format file et al, and accessing to
CIMISS and MICAPS CASSANDRA data web server.

提供对MICAPS文件, 卫星云图, 天气雷达等数据的读写, 并访问CIMISS和
MICAPS CASSANDRA数据库文件.

Only Python 3 is supported.

## Dependencies
Other required packages:

- numpy
- scipy
- xarray
- pandas
- pyproj
- protobuf
- urllib3
- python-dateutil

## Install
Using the fellowing command to install packages:
```
  pip install git+git://github.com/NMC-DAVE/dk_met_io.git
```

or download the package and install:
```
  git clone --recursive https://github.com/NMC-DAVE/dk_met_io.git
  cd dk_met_io
  python setup.py install
```