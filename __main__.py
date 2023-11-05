# -*- coding: utf-8 -*-
'''
Created on 21 juil. 2023

User friendly tool to cleanup your project folders/files.
Removes trailing spaces at the end of every line of your project for increased readability.
You only need to specify the root folder/file to cleanup, the program will explore everything recursively.

Works with python 3.6 and up.
Requires only one argument: the path (absolute or relative) to your source folder/file that you need to trim.

@author: BoxBoxJason
'''
import logging
import os
import sys
##---------- Trimming Functions ----------##

def trimFile(filePath):
    """
    Right trims all lines of the file
    """
    logging.debug(f"Trimming file {filePath}")
    try:
        with open(filePath,'r',encoding="utf-8") as readFile:
            editedFileList = []
            for line in readFile:
                editedFileList.append(line.rstrip())

        if editedFileList and editedFileList[-1] != "":
            editedFileList.append("")

        with open(filePath,'w',encoding="utf-8") as writeFile:
            writeFile.write("\n".join(editedFileList))

        logging.info(f"Successfully trimmed file at {filePath}")

    except UnicodeDecodeError:
        logging.fatal(f"Invalid encoding for file {filePath}, please convert to utf-8")


def trimChildren(dirPath):
    """
    Right trims all files at specified path
    """
    for childName in os.listdir(dirPath):
        childPath = os.path.join(dirPath,childName)
        if os.path.isdir(childPath):
            if os.access(childPath,os.R_OK):
                trimChildren(childPath)
            else:
                logging.error(f"Access denied to folder {childPath}")
        else:
            if os.access(childPath,os.R_OK) and os.access(childPath,os.W_OK):
                trimFile(childPath)
            else:
                logging.error(f"Read or Write permission denied for file {childPath}")


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
