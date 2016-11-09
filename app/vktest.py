import vk

vkAccessToken = ''
groupID = ''

def auth():
	session = vk.AuthSession(access_token = vkAccessToken)
	global api 
	api = vk.API(session)

def getWallPosts(count):
	return api.wall.get(owner_id = groupID, count = count)

def getComments(posts, num, count):
	return api.wall.getComments(owner_id = groupID, post_id = posts[num]['id'], need_likes = 1, count = count)