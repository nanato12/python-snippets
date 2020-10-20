# get-proxies-python
For use fake IP adress

## Description
下の参考URLの無料プロキシ取得を`bs4`を使用して取得するコードにし、IPやPortだけでなく他の値も取得できるように改善。

## Required modules
- [bs4](https://pypi.org/project/bs4/)

## How to use

```python
for proxy in get_proxies():
    print(proxy)
# {'IP': '200.152.78.48', 'Port': '38543', 'code': 'BR', 'country': 'Brazil', 'anonymity': 'elite proxy', 'google': False, 'https': True, 'refresh': '1 minute ago'}
# {'IP': '103.142.68.38', 'Port': '8080', 'code': 'BD', 'country': 'Bangladesh', 'anonymity': 'elite proxy', 'google': False, 'https': True, 'refresh': '1 minute ago'}
# {'IP': '139.255.123.194', 'Port': '4550', 'code': 'ID', 'country': 'Indonesia', 'anonymity': 'elite proxy', 'google': False, 'https': True, 'refresh': '1 minute ago'}  .....
```

## Reference
[https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/](https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/)
