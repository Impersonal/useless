import vk

class VkHelper:
	def __init__(self):
		session = vk.AuthSession()
		self.api = vk.API(session, v = '5.60')

	def _getId(self, shortID):
		return str(-self.api.groups.getById(group_id = shortID)[0]['id'])
		
	def getWallPosts(self, count, shortID):
		return self.api.wall.get(owner_id = self._getId(shortID = shortID), count = count)

	def getComments(self, posts, num, count, shortID):
		return self.api.wall.getComments(owner_id = self._getId(shortID = shortID), post_id = posts['items'][num]['id'], need_likes = 1, count = count)
