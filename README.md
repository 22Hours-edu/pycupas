# cupas

**cupas**는 쿠팡 파트너스 Open API의 Python Wrapper입니다.

https://github.com/22Hours-edu/pycupas
https://github.com/winterlood

## 사용 권한

쿠팡 파트너스의 Open API는, 판매 실적을 인정받은 회원에게만 제공되는 Access key와 Secret key를 필수 요청 값으로 지정하고 있습니다

따라서, 쿠팡 파트너스의 Key를 보유하고 있지 않다면 사용이 불가합니다.

## 기본 사용법

### import

```python
from pycupas import cupasApiDriver
```

다음과 같이 <code>cupasApiDriver</code>를 이용해 사용할 수 있습니다.

### Initializing

```python
cupas = cupasApiDriver.CupasApiDriver('access_key','secret_key')
```

다음과 같이 <code>CupasApiDriver</code>를 초기화 하신 뒤 사용할 수 있습니다 .

### Get Shorten Link

쿠팡 파트너스 수익으로 전환되는 단축 링크를 생성하는 API 입니다.

```python
subId = 'sub' # Optional
linkList = ['linkA','linkB'] #coupang 상품 페이지의 url 로 구성된 string list입니다.
cupas.get_cuplink(linkList,subId)

# linkList 는 필수
# subId는 optional
```
