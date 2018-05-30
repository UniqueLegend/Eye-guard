import os
import base64

magnet_head = 'magnet:?xt=urn:btih:'


def getThunderURL(url):
    return ("thunder://".encode("utf-8")+base64.b64encode(('AA'+url+'ZZ').encode("utf-8"))).decode("utf-8")

"""
if __name__ == "__main__":
    url = magnet_head + '83CEC2B2608CF10D89599764B4A1DC25A9C03847'
    thunder_URL = getThunderURL(url)
    os.system("\"D:\Program Files\ThunderSpeed\Program\Thunder.exe\" -StartType:DesktopIcon %s" % thunder_URL)
"""

