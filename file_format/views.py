from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os, shutil
import datetime

class FormatDirectoryAPI(APIView):
    

    def get(self, request, folder, *args, **kwargs):

        directory_exists = os.path.exists(folder)
        if not directory_exists:
            return Response({'message': "Directory does not exist"})

        entries = os.listdir(folder)
        for entry in entries:
            try:
                self.create_sub_folders(entry, folder)
            except:
                print("File format not supported")
                continue

        return Response({'message': "Directories created successfully"})

    def create_sub_directory(self, path):
        try: 
            os.makedirs(path, exist_ok = True) 
            print("Directory created successfully") 
        except: 
            print("Directory already exists") 

    def get_or_create_directory(self, dir_name, folder_name):
        parent_dir = os.path.abspath(dir_name)
        folder = os.path.join(parent_dir, folder_name)
        self.create_sub_directory(folder)
        return folder

    def create_sub_folders(self, entry, directory):

        td_date = datetime.datetime.now().strftime("%Y%m%d%H%M")
        file_format = entry.split('_')
        task_detail = file_format[2].split('.')
        folder_list = [td_date, file_format[0], file_format[0] + '_' + file_format[1], task_detail[0], task_detail[2]]
        project_name = file_format[0]

        if not os.path.exists(project_name):
            os.mkdir(project_name)

        parent_dir = project_name
        for folder in folder_list:
            parent_dir = self.get_or_create_directory(parent_dir, folder)

        shutil.copy(os.path.join(directory, entry), parent_dir)
  