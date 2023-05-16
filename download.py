import os
import urllib.request
from misc import LogConfig


def download_data(urls_arr, destination_folder):
    urls = urls_arr
    do_result = True

    if not isinstance(urls_arr, list):
        urls = [urls_arr]
    for url in urls:
        try:
            __download_file(url, destination_folder)
        except:
            LogConfig.LOGGER.error("Could not download file: {}".format(url))
            do_result = False
            break
    return do_result


def __download_file(url, dest):
    file_name = url.split('/')[-1]
    with urllib.request.urlopen(url) as response:
        with open(os.path.join(dest, file_name), 'wb') as f:
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = response.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)
