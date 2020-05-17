import requests
import json
from sys import stdin


class User:
    def __init__(self, user_id):
        uri = 'http://fg-69c8cbcd.herokuapp.com/user/{id}'
        uri = uri.format(id=user_id)
        r = requests.get(uri)
        data = json.loads(r.text)
        self.id = data['id']
        self.name = data['name']
        self.friends = data['friends']


if __name__ == '__main__':
    s = stdin.readline().rstrip()
    user = User(s)
    print(user.name)
    for f in user.friends:
        friend = User(str(f))
        print(friend.name)
