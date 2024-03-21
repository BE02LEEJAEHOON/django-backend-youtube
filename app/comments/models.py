from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# - User : FK
# - Video : FK
# - content
# - like , dislike

class Comment(CommonModel):
    content = models.TextField(default=0)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
