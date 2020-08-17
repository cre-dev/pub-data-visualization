
import os
import urllib
import zipfile
import errno
import pandas as pd
#
from . import url

def load_raw(year):
    fname_xls = url.fname_xls.format(year = year)
    fpath_xls = os.path.join(url.folder_raw,
                             fname_xls,
                             )
    try:
        if not os.path.isfile(fpath_xls): # try to download
            os.makedirs(url.folder_raw, exist_ok = True)
            fname_zip = url.fname_zip.format(year = year)
            fpath_zip = os.path.join(url.folder_raw,
                                     fname_zip,
                                     )
            url_zip = os.path.join(url.website,
                                   fname_zip,
                                   )
            urllib.request.urlretrieve(url_zip,
                                       fpath_zip,
                                       )
            with zipfile.ZipFile(fpath_zip, 'r') as zipObj:
                zipObj.extractall(os.path.dirname(fpath_xls))
            assert os.path.isfile(fpath_xls)
        df = pd.read_csv(fpath_xls,
                         header    = 0,
                         index_col = False, 
                         sep       = '\t', 
                         encoding  = 'latin-1',
                         na_values = ['ND'],
                         skipinitialspace = True,
                         low_memory = False,
                         )
    except FileNotFoundError:                    
        raise FileNotFoundError(
            errno.ENOENT,
            '\nFile not found : {0}\n'
            'It can sbe downloaded from \n'
            '{1}\n'
            'and stored in\n'
            '{2}'.format(fname_xls,
                         url.website,
                         url.folder_raw,
                         ))
    return df