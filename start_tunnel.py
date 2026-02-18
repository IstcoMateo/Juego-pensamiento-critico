from pyngrok import ngrok
import time

# Start an http tunnel on the same port as the local server (8000)
tunnel = ngrok.connect(8000)
print('Ngrok tunnel started:')
print(tunnel.public_url)
print('Press Ctrl+C to stop the tunnel...')
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('\nStopping tunnel...')
    ngrok.disconnect(tunnel.public_url)
    ngrok.kill()
    print('Tunnel stopped.')
