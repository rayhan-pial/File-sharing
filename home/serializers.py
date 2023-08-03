from rest_framework import serializers
from .models import *
import shutil

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False) #, user_url = False)
    )

    def zip_files(self, folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,'public/static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create( folder = folder , file = file)
            files_objs.append(files_obj)

        self.zip_files(folder.uid)

        return {'files_obj': {}, 'folder': str(folder.uid)}
