# -*- coding: utf-8 -*-

# pip install bing-image-downloader

# pip install simple-image-download

import os
from bing_image_downloader import downloader
import re

"""# Scrapping from bing"""

keywords = ["Hydroponic plant baskets", "Aeroponic plant roots", "Plant growth in aeroponics", "Aeroponic plant baskets"]

folders_names = list (map(lambda item : item.title(), keywords))
folders_names = list (map(lambda item : re.sub(r'\s+', '', item), keywords))

folders_names

for item in folders_names:
  os.mkdir(item, mode=777, dir_fd=None)

for keyword, folder in zip(keywords, folders_names):
  downloader.download(keyword, limit=100,  output_dir=folder, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)



