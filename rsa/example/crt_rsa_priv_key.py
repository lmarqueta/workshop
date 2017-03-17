import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64

def pempriv(n, e, d, p, q, dP, dQ, qInv):
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [0, n, e, d, p, q, dP, dQ, qInv]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodestring(der).decode('ascii'))

# Previously calculated data:
n = 1328067785708415296718856789612354571431144214353
d = 20061753022740301566316217400553821322431788033
e = 65537
p = 1165620213470141664679217
q = 1139365781719463002674209

dP = d % p
dQ = d % q
qInv = pow(q, p - 2, p)

pk = pempriv(n, e, d, p, q, dP, dQ, qInv)
print pk
