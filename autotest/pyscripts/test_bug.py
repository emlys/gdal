# test.py
import threading
import subprocess

import numpy
import requests
from osgeo import gdal


def test_bug():
    gdal.GetDriverByName('GTiff').Create('test.tif', 1, 1)

    for _ in range(164):  # the seg fault does not happen with fewer than 164 threads
        thread = threading.Thread(
            target=gdal.OpenEx,
            args=('test.tif',))
        thread.start()
        thread.join()

    requests.get('https://example.com')
    subprocess.run(['pwd'])
