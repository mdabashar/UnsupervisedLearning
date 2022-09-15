# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:09:18 2022

@author: basharm
"""

# Code to read csv file into Colaboratory:
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

class GoogleDriveFileHandler():
    
    def __init__(self):
        # Authenticate and create the PyDrive client.
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        self.drive = GoogleDrive(gauth)

    def download_file(self, gds_link, file_name):
        gid = gds_link.split('/')[-2]
        downloaded = self.drive.CreateFile({'id':gid})
        downloaded.GetContentFile(file_name)