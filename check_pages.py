import urllib.request
import time

url = 'https://IstcoMateo.github.io/Juego-pensamiento-critico/noticia-cerebro-final.html'
attempts = 8
wait = 15

print(f'Checking {url} up to {attempts} times (every {wait}s)...')
for i in range(1, attempts+1):
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            code = r.getcode()
            if code == 200:
                print(f'OK: {url} (HTTP {code})')
                exit(0)
            else:
                print(f'Attempt {i}: HTTP {code}')
    except Exception as e:
        print(f'Attempt {i}: not ready ({e})')
    if i < attempts:
        time.sleep(wait)
print('Not available yet.')
exit(2)
