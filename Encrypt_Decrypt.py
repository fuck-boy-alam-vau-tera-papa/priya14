# Encrypted by MrK4US4R
# Whatsapp 01612278337 
# Github- https://github.com/MrK4US4R

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))