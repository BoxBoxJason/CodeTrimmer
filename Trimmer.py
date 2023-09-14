# -*- coding: utf-8 -*-
'''
Created on 21 juil. 2023

@author: BoxBoxJason
'''
import logging
import os

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
