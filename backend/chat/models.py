from tkinter import CASCADE
from django.db import models
from users.models import User
from post.models import *

class Chatroom(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    questioner = models.ForeignKey(User, related_name='questioner', on_delete=models.CASCADE)
    answerer = models.ForeignKey(User, related_name='answerer', on_delete=models.CASCADE)
       
    def opponent(self, current_user):
        if current_user == self.questioner:
            return self.answerer
        else :
            return self.questioner
    def is_user_in_talkers(self, current_user):
        result = False
        if current_user == self.questioner:
            result = True
        if current_user == self.answerer:
            result = True
        return result
    def topic(self):
        return self.post.title

class Chat(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)