from flask import Flask

app = Flask(__name__)

from app import vkhelper

vk = vkhelper.VKHelper() 

from app import views
