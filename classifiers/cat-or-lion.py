import ssl
import sys
from time import sleep
from duckduckgo_search import ddg_images
from fastcore.all import *
from fastdownload import download_url

# SSL Setup
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# First we need to download images of cats and lions
# with varying lighting conditions.

def search_images(term, max_imgs=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_imgs)).itemgot('image')

# Now we will search for some lions and cat images:
# Let's compile a list of URL's then we can feed those URL's into the downloader fn:

def download_images(term: str, urls: list):
    for idx, img in enumerate(urls):
        download_url(img, f"./{term}/{term}-{idx}.png")
        # Minor sleep so as to not overload the server:
        sleep(2)

def run_downloader(mode: str):
    match mode:
        case "lions":
            download_images('lions', search_images('photos of lion', max_imgs=10))
        case "cats":
            download_images('cats', search_images('pitcures of majestic of cats', max_imgs=10))
        case "both":
            download_images('lions', search_images('photos of lion', max_imgs=10))
            download_images('cats', search_images('pitcures of majestic of cats', max_imgs=10))
        case _:
            print("Skipping download")

if (len(sys.argv)>1):
    run_downloader(sys.argv[1])