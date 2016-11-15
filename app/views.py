from app import app
from app import vk

@app.route('/<group_id>')
def parse(group_id): 
	commentList = vk.getComments(posts = vk.getWallPosts(count = 3, short_id = group_id), num = 2, count = 100, short_id = group_id)
	res = ''
	for i in commentList['items']:
		res += (i['text'] + 2 * '<br/>').encode("utf-8")
	return res
