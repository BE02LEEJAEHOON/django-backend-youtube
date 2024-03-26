from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video
from django.db.models import Count, Q
# - User : FK
# - Video : FK
# - reaction (like, dislike, cancel) -> choice 사용

class Reaction(CommonModel):
    # circular import error
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.video', on_delete=models.CASCADE)
    
    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0
    
    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )
    
    reaction = models.IntegerField(
        choices = REACTION_CHOICES,
        default = NO_REACTION
    )
    
    @staticmethod # ORM depth2
    def get_video_reaction(video): # 1번 비디오 - 좋아요/싫어요 갯수 궁금
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE)),
            
        )
        
        return reactions


    