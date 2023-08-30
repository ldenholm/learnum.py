import sys
import fastbook
from fastbook import *
from fastai.vision.widgets import *

def main():
    #fastbook.setup_book()
    key = sys.argv[1]
    bear_types = 'grizzly','black','teddy'
    path = Path('bears')
    fns = get_image_files(path)
    failed = verify_images(fns)
    print(failed)
    failed.map(Path.unlink)
    # for o in bear_types:
    #     dest = (path/o)
    #     dest.mkdir(exist_ok=True)
    #     results = search_images_bing(key, f'{o} bear')
    #     download_images(dest, urls=results.attrgot('contentUrl'))

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------
#results = search_images_bing(key, 'grizzly bear')
#ims = results.attrgot('contentUrl')
#print('first entry in ims', ims[0])
#

# if not path.exists():
#     path.mkdir()
#     for o in bear_types:
#         dest = (path/o)
#         dest.mkdir(exist_ok=True)
#         results = search_images_bing(key, f'{o} bear')
#         download_images(dest, urls=results.attrgot('contentUrl'))
#-------------------------------------------------------------------------------------