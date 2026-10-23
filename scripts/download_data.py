import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
from inf8239_u03.config import MOVIELENS_URL, ROOT
from inf8239_u03.data import download_zip

destination, digest = download_zip(MOVIELENS_URL, ROOT / "data/raw")
print("Destino:", destination)
print("SHA-256:", digest)
