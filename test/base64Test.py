import base64

# a1="xianRE:( "
#
# deCod = base64.b64decode(a1)
# print  deCod
#
# a2="xianRE:( "
# enCod = base64.b32encode(a2)
# print enCod

# a3 = "R@WUA1QQKW7ASKC?"
# deCod = base64.b32decode(a3)
# print deCod


encoded_data = ["bWFpbigpe2ludCBpLG5bXT17KCgoMSA8PDEpPDwgKDE8PDEpPDwoMTw8Cm==",
                "ICAgICAgIDEpPDwoMTw8KDE+PjEpKSkrKCgxPDwxKTw8KDE8PDEpKSksKCgoMQp=",
                "ICAgICAgIDw8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAxKQq=",
                "ICAgICAgIDw8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoMQp=",
                "ICAgICAgIDw8MSk8PCgxPDwxKTw8ICAgICAgICAgKDE8PDEpKS0oKDE8PDEpPDwoCr==",
                "ICAgIAkxPDwxKTw8KDE8PDEpKSsgICAgICAgICgoMTw8MSk8PCgxPDwoMT4+Ch==",
                "ICAgICAgIDEpKSkrKDE8PCgxPj4xKSkpICAgICAgICAgICAgICAgICAgICAgICAgLAq=",
                "ICAgICAgICgoKDE8PDEpPDwoMTw8MSkgICAgICAgICAgICAgICAgICAgICAgICA8PAo=",
                "ICAgICAgICgxPDwxKTw8KDE8PDEpKS0oKDEgPDwxKTw8KDE8PDEpIDw8KDE8PCgxCl==",
                "ICAgICAgID4+MSkpKS0oKDE8PDEpPDwoMTw8KDE+PjEpKSkpLCgoKDE8PDEpCp==",
                "ICAgICAgIDw8KCAgICAxPDwgICAgICAgICAgICAgICAgICAgICAgICAgIDEpCt==",
                "ICAgICAgIDw8KCAgICAxPDwgICAgICAgICAgICAgICAgICAgICAgICAgIDEpCu==",
                "ICAgICAgIDw8KCAxPDwxKSktKCgxIDw8MSk8PCAoMSA8PDEpPDwoMSA8PAr=",
                "ICAgICAgICgxPj4xKSkpLSgoMTw8MSk8PCgxPDwoMT4+MSkpKSksKCgoMTw8MSk8PAo=",
                "ICAgICAgICgxPDwxKTw8KDE8PDEpPDwoMTw8MSkpLSgoMTw8MSk8PCgxPDwxKTw8KAr=",
                "ICAgICAgIDE8PCgxPj4xKSkpLSgxPDwoMT4+ICAgICAgICAgIDEpKSksKCgoMTw8MSk8PAq=",
                "ICAgICAgICgxPDwxKTw8KDE8PDEpKSsgICAgKCgxPDwxKSAgICA8PCgxPDwxKTw8Ch==",
                "ICAgICAgICgxPDwoMT4+MSkpKS0oKCAgICAgMTw8MSk8PCggICAgICAxPDwoMT4+Co==",
                "ICAgICAgIDEpKSkpLCgoMTw8MSk8PCAgICAgICgxPDwxKSAgICAgICAgPDwoMTw8MSkpCl==",
                "ICAgICAgICwoKCgxPDwxKTw8KDE8PCAgICAgIDEpPDwoICAgICAgIDE8PDEpPDwoMTw8MSkpLQr=",
                "ICAgICAgICgoMTw8MSk8PCgxPDwxKSAgICAgKS0oMTw8KDE+PjEpICAgICAgKSksKCgoCj==",
                "ICAgICAgIDE8PDEpPDwoMTw8MSk8PCggICAgMTw8MSk8PCgxPDwxKSktICAgICgoMQp=",
                "ICAgICAgIDw8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgMQq=",
                "ICAgICAgICkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8PAp=",
                "ICAgICAgICgxPDwxKTw8KDE8PCgxPj4xKSkpLSgxPDwoMT4+MSkpKSwgKCgoMTw8MQp=",
                "ICAgICAgICk8PCgxPDwxKTw8KDE8PDEpPDwoMTw8MSkpLSgoMTw8MSk8PCAoMSAgCk==",
                "ICAgICAgIDw8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAxCp==",
                "ICAgICAgICkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDw8Cn==",
                "ICAgICAgICggICAgIDE8PCgxPj4xKSkpKyAgICAoMTw8MSkpLCgoKDEgICAgIDw8Cj==",
                "ICAgICAgIDEpICAgIDw8KDE8PDEpPDwgICAgICAoMTw8MSk8PCgxICAgICAgIDw8Ck==",
                "ICAgICAgIDEgICAgICkpLSgoMTw8MSk8PCAgICAoMTw8MSk8PCgxICAgICAgIDw8Cj==",
                "ICAgICAgICggICAgIDE+PjEpKSktKCgxICAgICAgPDwxKTw8KDE8PCAgICAgICAoCj==",
                "ICAgICAgIDEgICAgID4+MSkpKSksKCgoMSAgICAgPDwxKTw8KDEgICAgICAgIDw8Cg==",
                "ICAgICAgIDEgICAgICk8PCgxPDwxKTw8KCAgICAgMTw8MSkpLSgoMSAgICAgIDw8Cm==",
                "ICAgICAgIDEgICAgICk8PCgxPDwxKTw8ICAgICAoMTw8MSkpKygoICAgICAgICAxCv==",
                "ICAgICAgIDw8MSk8PCgxPDwoMT4+MSkpKSksKCgoMTw8MSk8PCgxPDwxKSA8PCgxCm==",
                "ICAgICAgIDw8MSkpKygxPDwoMT4+MSkpKSwoKCgxPDwxKTw8KDE8PDEpKSArKCgxCs==",
                "ICAgICAgIDw8MSk8PCAoMTw8KDE+PjEpKSkgKyAoMTw8ICgxPj4xKSkpfSA7Zm9yCn==",
                "ICAgICAgIChpPSgxPj4xKTtpPCgoKDE8PDEpPDwoMSA8PDEpKSsoKDEgPDwxKTw8KAr=",
                "ICAgICAgIDE8PCgxPj4xKSkpKygxPDwxKSk7aSsrKSAgcHJpbnRmKCIlYyIsbltpXSk7fQp=", ]

normal_data = [e.decode("base64").encode("base64").rstrip()
               for e in encoded_data]
base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
flag = ""

for e, n in zip(encoded_data, normal_data):
    diff = base64chars.index(e[e.index("=") - 1]) - \
        base64chars.index(n[n.index("=") - 1])
    equalnum = e.count('=')  # no equalnum no offset
    if equalnum:
        flag += bin(diff)[2:].zfill(equalnum * 2)
    print "%x" % (int(flag, 2))

print "[+] Flag: %s" % (("%x" % int(flag, 2)).decode("hex"))
