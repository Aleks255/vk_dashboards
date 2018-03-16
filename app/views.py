from django.shortcuts import render
from .models import MyVkData
from datetime import datetime
import vk

# Create your views here.

def posts(request):

	session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.PASSW)
	vkapi = vk.API(session)

	countPage = 0
	posts = vkapi.wall.get(owner_id='-57846937', count=10, offset=countPage, v=5.73)

	context = {}
	n = 0
	for post in posts['items']:
		n += 1
		date = datetime.fromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M:%S')
		likes = post['likes']['count']
		comments = post['comments']['count']
		reposts = post['reposts']['count']
		context['key_' + str(n)] = {"date": date}

	return render(request, 'index.html', context)


def post(request, p):

	session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.PASSW)
	vkapi = vk.API(session)

	countPage = p
	post = vkapi.wall.get(owner_id='-57846937', count=1, offset=countPage, v=5.73)['items'][0]

	likes = post['likes']['count']
	comments = post['comments']['count']
	reposts = post['reposts']['count']
	context = {'data': [likes, comments, reposts], 'num_post': countPage}

	return render(request, 'graph.html', context)
