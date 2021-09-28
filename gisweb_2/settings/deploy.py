from .base import *

# 도커 secret으로 대체
# local_env = open(os.path.join(BASE_DIR,'.env'))
#
# env_list = dict()
# while True:
#     line = local_env.readline()
#     if not line:
#         break
#     key,value = line.split("=")
#     env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    # 혹시 모를 공백지우기
    secret = secret.lstrip().rstrip()
    # 파일 스트림 닫기
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env_list['SECRET_KEY']
SECRET_KET = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}

