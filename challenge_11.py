import zlib
filepath = r'./challenges/challenge 11/generated_content/63.zlib'
with open(filepath, 'rb') as handle:
    stuff = handle.read()
    # print(zlib.decompress(stuff))
    dc_obj = zlib.decompressobj()
    out = dc_obj.decompress(stuff)
    print(out)