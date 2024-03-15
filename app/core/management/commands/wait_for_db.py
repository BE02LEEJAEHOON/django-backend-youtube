# Django가 DB 연결에 실패했을 경우, 재시도를 하도록 만드는 로직을 추가
from django.core.management.base import BaseCommand
from django.db import connections
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB connection ...')
        
        is_db_conneted = None
        while not is_db_conneted:
            try:
                is_db_conneted= connections['default']
            except:
                self.stdout.write('Retrying DB connection ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('PostgreSQL DB Connection Success !!!'))
        