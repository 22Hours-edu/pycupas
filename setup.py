from setuptools import setup, find_packages
from os import path

this = path.abspath(path.dirname(__file__))
with open(path.join(this, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
name='pycupas',
version='1.0.6',
author='winterlood',
author_email='winterlood@22hours.co.kr',
url='https://github.com/winterlood',
description='Make your own coupang partners bot easily',
license='MIT',
py_modules=['cupasApiDriver'], # 패키지에 포함되는 모듈
python_requires='>=3',
install_requires=[], # 패키지 사용을 위해 필요한 추가 설치 패키지
packages=['pycupas'], # 패키지가 들어있는 폴더들
long_description=long_description,
long_description_content_type='text/markdown',
)