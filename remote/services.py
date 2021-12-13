import json
from django.conf import settings
from zoomus import ZoomClient


class Users():
    """ Create Zoom User object """
    def __init__(self):
        self.id = ""
        self.fname = ""
        self.lname = ""
        self.email = ""
        self.pmi = ""

# Obtain users from Zoom api and extract required data
def get_users():
    client = ZoomClient(settings.ZOOM_API, settings.ZOOM_SECRET)

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    users = []

    for user in user_list['users']:
        user_id = user['id']
        data = json.loads(client.user.list(user_id=user_id).content)
        for item in data['users']:
            remote_user = Users()
            remote_user.id = item['id']
            remote_user.fname = item['first_name']
            remote_user.lname = item['last_name']
            remote_user.email = item['email']
            remote_user.pmi = item['pmi']
            users.append(remote_user)
        return users
