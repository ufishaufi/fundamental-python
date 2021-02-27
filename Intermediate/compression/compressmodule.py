import zlib, base64

def compress(inputFile, outputFile):
    data = open(inputFile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputFile, 'w')
    compressed_file.write(decoded_data)

def decompress(inputFile, outputFile):
    file_content = open(inputFile, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompress_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompress_data.decode('utf-8')
    file = open(outputFile, 'w')
    file.write(decoded_data)
    file.close()

# compress('demo_speech.txt','ot.txt')
decompress('ot.txt','dc1.txt')