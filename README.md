# GY4
## NetCat
> szerverként: `nc` és az `1234` porton akkor és `localhost`-on `nc -l 1234`

> kliens `nc localhost 1234`

vagy `nc google.com 80` és akkor a googlehöz kaplcsolódunk HTTPként

Lokális webszerver is lehet:
szerver netcat: `nc -l 12345` ammihez a böngésző `localhost:12345`ton kersztül kapcsolódik

## tcpdump
  interface: `-i`
  localhost: `lo`
  fáklbamentés: `-w`

`openwrt` és `ddwrt` fimrwarek a routeren támogatják, hogy különböző plusz funkciókat használjunk.

## Wireshark
 
## server - kliens socketek
- a server és a kliens is csinál magának azonos típusú socketet
- s erver `bind`ol egy portra és vár
- a kliens `connect`al
- mindkét fél küldhet és fogadhat `send` vagy `recieve`vel
- a socketet mindkét oldal kérheti bezárásra, viszont akkor minkét oldalt zárjuk be

használathoz: `import socket`
saját hosztname: `socket.gethostname()`
serverről: `gethostbyname()`
ipcímről a hostneve: `gethostbyaddr()`

szerveroldalon megmondjuk, ohgy a socketet mire használjuk: `server_address=('localhost',1000)` ekkor az 1000es porton fog localhoston hallgatózni a `sock.bind(server_address)` miatt
a hallgatózást a `sock.listen(1)`
a socketen ahol hallgatok várom a klienst: `sock.accept()`

````Python
import socket
sock = socket.socket(socket.AF_INET, socket....
````
