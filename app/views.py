from app import app
from app import vkhelper

@app.route('/<groupID>')
def parse(groupID):
	vk = vkhelper.VkHelper(shortid = groupID) 
	commentList = vk.getComments(posts = vk.getWallPosts(count = 3), num = 2, count = 100)
	res = ''
	commentList.pop(0)
	for i in commentList:
		res += (i['text'] + 2 * '<br/>').encode("utf-8")
	return res
