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
## Feladatok
### egyszerű kliens-server
- kliens kapcsolódik az `12345` porton a `localost`hoz és elküldi a `kerdes` szót mire a server `valasz` szóval válaszol.
> fájl: `testserverclient.py` és `testserver.py`

### egyszerű chatprogram
- kliens a konzolon kapott értéket átküldi, a server a konzolon kap választ és azt átküldi így megy `exit`ig
> fájl: `chatclient.py` és `chatserver.py`

### számológép
- a kliens két számot küld és egy operátort egymás után külön-külön, majd a server azt feldolgozza és visszaküldi a műveletek eredményét
> fájl (mintamegoldás): `calculator.py` és `client.py` valamint azok 3-mas verziójú megoldása.
