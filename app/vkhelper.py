import vk


class VKHelper:
	def __init__(self):
		session = vk.AuthSession()
		self.api = vk.API(session, v = '5.60')

	def __getID(self, short_id):
		return str(-self.api.groups.getById(group_id = short_id)[0]['id'])
		
	def getWallPosts(self, count, short_id):
		return self.api.wall.get(owner_id = self.__getID(short_id = short_id), count = count)

	def getComments(self, posts, num, count, short_id):
		return self.api.wall.getComments(owner_id = self.__getID(short_id = short_id), post_id = posts['items'][num]['id'], need_likes = 1, count = count)
