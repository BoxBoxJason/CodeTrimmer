# -*- coding: utf-8 -*-
'''
Created on 21 juil. 2023

@author: BoxBoxJason
'''
import logging
import os
import sys

from Trimmer import trimChildren
from Trimmer import trimFile

##---------- Logging setup ----------##
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(__file__),"logging.log")),
        logging.StreamHandler(sys.stdout)
    ]
)

##---------- Argument Parser ----------##
if len(sys.argv) != 2:
    logging.fatal(f"Incorrect number of arguments ({len(sys.argv) -1}/1)\n\
    Please just provide source folder/file path")
    sys.exit(1)

rootFolderPath = sys.argv[1]

if os.path.exists(rootFolderPath) and os.access(rootFolderPath,os.R_OK):
    if os.path.isdir(rootFolderPath):
        trimChildren(rootFolderPath)
    else:
        trimFile(rootFolderPath)
    logging.info(f"End of trimming, check if everything went smooth in {rootFolderPath}")
else:
    logging.fatal(f"File or directory not found or access denied at {rootFolderPath}")
