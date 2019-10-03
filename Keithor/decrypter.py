from base64 import *
from hashlib import *

test = b'NVL7OA'
#test = md5(test).hexdigest() 32 bytes long
#test = sha1(test).hexdigest() 40 bytes long
#test = sha224(test).hexdigest() 56 bytes long
#test = sha256(test).hexdigest() 64 bytes long
#test = sha384(test).hexdigest() 96 bytes long
#test = sha512(test).hexdigest() 128 bytes long
print b64encode(test)
#4f79807a7c47f697bd5f06beef955cfdf4fdaef8ade8edf707858fe4294d780d69d4d6a897d8598ce3142d207640ca51d8215d0d6c693873fd32c1f6e468750027b5db34b7d9ce0a79753ecc73da664a995889e0d36db4bfc68df9fc8da3d369b266e617a6158d16ccad4189f0a3dcae62d9b103b50b0d4337c96163471b423fc28f3cda29417b7280eb9321492075c5890dc033471cf91781a07001cea6696b32cdf56b2129bc76a83218bee52c830a8bfc09ec55ae372110c0cc8950ef577d32ed211d40307c3fd6684113341e603c
#md4=4f79807a7c47f697bd5f06beef955cfd
