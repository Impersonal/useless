import vk

class VkHelper:
	def __init__(self, shortid):
		session = vk.AuthSession()
		self.api = vk.API(session)
		self.id = str(-self.api.groups.getById(gid = shortid)[0]['gid'])

	def getWallPosts(self, count):
		return self.api.wall.get(owner_id = self.id, count = count)

	def getComments(self, posts, num, count):
		return self.api.wall.getComments(owner_id = self.id, post_id = posts[num]['id'], need_likes = 1, count = count)