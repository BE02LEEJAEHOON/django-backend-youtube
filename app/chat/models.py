from django.db import models
from common.models import CommonModel

# ChatRoom 모델을 분리했을 때의 이점
# - 관리의 용이
# - 확장성 (채팅방 : 오픈채팅방, 업무채팅방-비밀번호 입력 등등)

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)
    


class ChatMessage(CommonModel):
    # SET_NULL : sender null 값으로 두겠다는 뜻. 1번 -> 계정삭제 -> null
    sender = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    
    
# User:Msg(FK) => 1:N
    # - User : Msg, Msg, Msg, Msg => O
    # - Msg : User, User, User, User => X


# Room:Msg(FK) => 1:N ( 룸은 부모, 메세지는 자녀가 된다.)
    # - Room : Msg, Msg, Msg, Msg => O
    # - Msg = Room, Room, Room, Room  => X

