# Achived
Please use https://github.com/likev/nmc_met_io instead.

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

## 设置CIMISS和MICAPS服务器的地址及用户信息
在系统用户目录下(如"C:\Users\用户名"), 新建文本文件config_dk_met_io.ini, 里面内容模板为:
```
[CIMISS]
DNS = xx.xx.xx.xx
USER_ID = xxxxxxxxx
PASSWORD = xxxxxxxx

[MICAPS]
GDS_IP = xx.xx.xx.xx
GDS_PORT = xxxx
```
这里xxxx用相应的地址, 接口和用户信息代替.
