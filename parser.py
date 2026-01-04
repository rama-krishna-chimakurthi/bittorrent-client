import pprint

def parse_integer(data, index):
    assert data[index:index+1] == b'i'
    index += 1
    end = data.index(b'e', index)
    return int(data[index:end]), end+1

def parse_list(data, index):
    assert data[index:index+1] == b'l'
    index+=1
    l = []
    while index < len(data) and data[index:index+1] != b'e':
        val, index = parse_any(data, index)
        l.append(val)
    return l, index+1



def parse_dict(data, index):
    assert data[index:index+1] == b'd'
    index = index + 1
    d = {}
    while index < len(data) and data[index:index+1] != b'e':
        key, index = parse_string(data, index)
        val, index = parse_any(data, index)
        d[key] = val
    return d, index+1

def parse_string(data, i):
    j = data.index(b":", i)
    length = int(data[i:j])
    j+=1
    s = data[j : j + length]
    return s, j + length

def parse_any(data, index):
    ch = data[index:index+1]
    if ch == b'i':
        return parse_integer(data, index)
    if ch == b'l':
        return parse_list(data, index)
    if ch == b'd':
        return parse_dict(data, index)
    if chr(data[index]).isdigit():
        return parse_string(data, index)
    

def bdecode(data):
    if not data:
        raise ValueError("Empty data cannot be decoded")
    if not isinstance(data, bytes):
        raise TypeError("Data must be of type bytes")
    val, i = parse_any(data, 0)
    if i<len(data):
        raise IndexError("Not parsed properly")
    return val

with open('test.torrent', 'rb') as f:
    torrent_data = f.read()

decoded = bdecode(torrent_data)
pprint.pprint(decoded[b'announce'])