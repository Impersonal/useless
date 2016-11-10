from app import app
from app import vk

@app.route('/<groupID>')
def parse(groupID): 
	commentList = vk.getComments(posts = vk.getWallPosts(count = 3, shortID = groupID), num = 2, count = 100, shortID = groupID)
	res = ''
	commentList.pop(0)
	for i in commentList:
		res += (i['text'] + 2 * '<br/>').encode("utf-8")
	return res
