# _*_ coding: utf-8 _*_

"""
Read configure file
"""

import os
import configparser


def ConfigFetchError(Exception):
    pass


def _get_config_from_rcfile():
    """
    Get configure information from config_dk_met_io.ini file.
    """
    rc = os.path.normpath(os.path.expanduser("~/config_dk_met_io.ini"))
    try:
        config = configparser.ConfigParser()
        config.read(rc)
    except IOError as e:
        raise ConfigFetchError(str(e))
    except Exception as e:
        raise ConfigFetchError(str(e))

    return config
