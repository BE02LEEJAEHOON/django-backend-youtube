from django.test import TestCase
from django.contrib.auth import get_user_model


# TDD (User 관련 테스트 코드)
# TDD (Test Drvien Development (채용공고에 TDD 우대)

class UserTestCase(TestCase):
    
    # 일반 유저 생성 테스트
    def test_create_user(self):
        email = 'ljhx6787@naver.com'
        password = '123'
        
        user = get_user_model().objects.create_user(email=email, password=password)
        
        # 유저가 정상적으로 잘 만들어졌는지
        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        # self.assertEqual(user.is_superuser, False)
        self.assertFalse(user.is_superuser)
        # users 테스트 코드 실행 명령어    
        # docker-compose run --rm app sh -c 'python manage.py test users'
    
    
    
    # 슈퍼 유저 생성 테스트
    def test_create_superuser(self):
        email = 'ljhx6787_super@naver.com'
        password = '123'
        
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        # 슈퍼유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        