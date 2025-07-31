import ssl, socket

## HTTPS portuna bağlan
hostname = "google.com"
context = ssl.create_default_context()
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())  ## Örn: TLSv1.3
