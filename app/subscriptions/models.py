from django.db import models
from common.models import CommonModel
from users.models import User

# - User : FK -> subscriber (내가 구독한 사람)
# - User : FK -> subscribed_to (나를 구독한 사람)

# User:Subscription -> User(subcriber) -> subcriber, subcriber, subcriber, subcriber(FK)
# User:Subscription -> User(subcribed_to) -> subcribed_to, subcribed_to, subcribed_to(FK)

class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    
    # subscriver_set -> subscriptions (내가 구독한 사람들)
    # subscribed_to_set -> subscribers (나를 구독한 사람들)