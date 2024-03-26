from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction


class VideoListSerializer(serializers.ModelSerializer):
    # Video:User -> Video(FK) -> User
    user = UserSerializer(read_only=True) # Video(FK)
    
    # Video:Comment -> Video -> Comment(FK)
    # - Reverse Accessor
    # - 부모가 자녀를 찾을 때 -> _set
    
    class Meta:
        model = Video
        fields = '__all__' 
        # depth = 1 
        
        
class VideoDetailSerializer(serializers.ModelSerializer):
    # Video:User -> Video(FK) -> User
    user = UserSerializer(read_only=True) # Video(FK)
    
    # Video:Comment -> Video -> Comment(FK)
    # - Reverse Accessor
    # - 부모가 자녀를 찾을 때 -> _set
    comment_set = CommentSerializer(many=True, read_only=True)
    
    reactions = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = '__all__'
        
        # depth = 1 
        
    def get_reactions(self, video):
        return Reaction.get_video_reaction(video) # 비디오 줄게 -> 리액션 내놔~