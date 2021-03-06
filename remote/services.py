from django.db import models
from django.conf import settings

import json
import logging
from zoomus import ZoomClient
from remote import graph_api

class Video():
    """ Create Video object """
    def __init__(self):
        self.id = ""
        self.type = ""
        self.name = ""
        self.url = ""


class Users():
    """ Create Zoom User object """
    def __init__(self):
        self.id = ""
        self.fname = ""
        self.lname = ""
        self.pmi = ""
        self.exclude = ""

# Obtain users from Zoom api and extract required data
def get_users():
    client = ZoomClient(settings.ZOOM_API, settings.ZOOM_SECRET)

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    users = []

    for user in user_list['users']:
        user_id = user['id']
        data = json.loads(client.user.list(user_id=user_id, page_size=100, include_fields='custom_attributes').content)
        for item in data['users']:
            remote_user = Users()
            remote_user.id = item['id']
            remote_user.fname = item['first_name'].title()
            remote_user.lname = item['last_name'].title()
            remote_user.pmi = "https://zoom.us/j/" + str(item['pmi'])
            for custom in item['custom_attributes']:
                remote_user.exclude = custom['value']
            if not remote_user.exclude:
                users.append(remote_user)
        return users



def get_video(request):
    video_data = graph_api.one_drive(request)
    content = []
    for video in video_data['value']:
        if 'video' in video:
            videos = Video()
            videos.id = video['id']
            videos.type = request
            videos.name = video['name']
            videos.url = video['@microsoft.graph.downloadUrl']
            content.append(videos)
    return content