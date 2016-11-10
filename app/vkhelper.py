import vk

class VkHelper:
	def __init__(self):
		session = vk.AuthSession()
		self.api = vk.API(session)

	def _getId(self, shortID):
		return str(-self.api.groups.getById(gid = shortID)[0]['gid'])
		
	def getWallPosts(self, count, shortID):
		return self.api.wall.get(owner_id = self._getId(shortID = shortID), count = count)

	def getComments(self, posts, num, count, shortID):
		return self.api.wall.getComments(owner_id = self._getId(shortID = shortID), post_id = posts[num]['id'], need_likes = 1, count = count)
