from app import app
from app import vktest

@app.route('/')
@app.route('/index')
def index():
	vktest.auth() 
	commentList = vktest.getComments(posts = vktest.getWallPosts(50), num = 2, count = 100)
	i = 1
	res = ''
	while i <= commentList[0]:
		res += (commentList[i]['text'] + '<br/>').encode("utf-8")
		i += 1
	print str
	return res
