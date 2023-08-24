# First we need to download images of cats and lions
# with varying lighting conditions.

from time import sleep
import DuckDuckGoImages as ddg
from duckduckgo_search import ddg_images
from fastcore.all import *
from fastdownload import download_url

def search_images(term, max_imgs=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_imgs)).itemgot('image')

# Now we will search for some lions and cat images:
# Let's compile a list of URL's then we can feed those URL's into the downloader fn:

urls = search_images('photos of lion', max_imgs=10)
for url in urls:
    print(url)

def download_images(term: str, urls: list):
    for idx, img in enumerate(urls):
        download_url(img, f"{term}-{idx}")
        # Minor sleep so as to not overload the server:
        sleep(2)

download_images('lion', urls)