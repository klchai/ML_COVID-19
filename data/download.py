import os
import sys
import socket
import urllib
import urllib.request

def download(url, path):
    socket.setdefaulttimeout(30)
    if not os.path.exists(path):
        try:
            print("Download job begin.")
            urllib.request.urlretrieve(url, path)
            print("Download job finished.")
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.urlretrieve(url, path)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count ==1 else 'Reload for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                    print("download job failed")
