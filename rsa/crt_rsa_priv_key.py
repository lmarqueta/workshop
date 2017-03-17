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

# Sample data:
n = 0x00d078004d524e0d7635eb71eaa640bc26d49e9049
d = 0xc139c945e1f8d8bf6ddf3e76f7c778c8f4112bb5L
e = 65537
p = 1083490222393316586230927
q = 1083490222393316586230927

dP = d % p
dQ = d % q
qInv = pow(q, p - 2, p)

pk = pempriv(n, e, d, p, q, dP, dQ, qInv)
print pk
