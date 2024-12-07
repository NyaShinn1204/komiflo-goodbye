import base64, json, math, random, time, re

key_data = "InpyTl8cdwFRB35BaWBEcFABYwlQdwhaUEsHRFRzBQwzFE5LW0stQ0EHAkJQTgccBlRbSVldQkhOQ0FHVQBAW0EtRhJZQEhSaFZbX0sGRVIDQF4NDQFRT1kPXEQMVU5HAQBXbRoXU1NHCmJaU1dVCw8GH1kFDVdVDgNNCgVXVlMFBzlNQQZRQQhoCQZSBFADUg1PBwkEAQVYXANKBQYCV2huclQ4a2QCUBB8LGtoUXFTBm4CTnYJT1FLBEVWbQwNVwheTUFEK15TAAdQUywGAANRWkxfUlZIUkZERl0DQEdJQF4FUENbWm5LTFZGFEw6D1xaDgwJUFRWB0VDCl5GWg4GVggEAFI/SRIIVEZYPQIHBwtZAAxWSAYFUAoKW1ZVGAFVUFsOVloFbhQUUAVADToNWgcAAwYMTVwIVwwOAlZ1YXteVXVyBj4eZEZielIaUwNuBlFxC0ZNSAVJVXUODl8UXUpBR0RLQwJuXktGDhINP1xKX1JLQVRAXUBWBkFZTUZTHFlCXVEAVV5eLhpUUxRWNAEGDFBPWg5cTApYR0QOAE8JBQBQW1MAZE5GUFYRDG0CUwYIXFEABE0DAFZTVQwGVU1SBVdTBQQLBTweQAVQFlltCAUEDFlVBlIYBwNSYW9xWlBrdwFQCnFFaW81bUABZBJYHAhGU0kNQlV3EQxeClxCQENPXkABAUJeQgUBakhPSltJQCJTQ0VGUQNKXlRBWwRfRVNaBUtfVkcBQFEDWDIUFwtVWlVsQUQLVERDBA5PAQcHW1BVCAxOVVNUCgcHC1hvFEZWAhZbaQNTVFUDBlRWTwZSVAUECQBRHlMGVgNVAQ4BahhDVwdEDm0AUGtrc1hdf2oCUgB1RWhoX21TAmQDUHQKQzxVF0NUYwdmXwlYQk1BT0ddAAJGUUQCAANIXElcU05AU0AsXUYDQElCK1sCXEZYXQVRQlZBAkBTDlRWFAQLVU5cBUdGZEFURA4UWWsHBVZTVgYBU0hTVgcHBQFVBBRVVAMFUwoEUD5OFgNGWzgGU1sEBAEPUR5TB1kCWwAAABsFUV0HUAMBBjx1enZOXxxxCloKc05pdF94WwpmBVZrDk9YTgxBURwRH1saViFIQUFBRwQBQ0VGBwcEUVRMWkdLSVVBRkJRASVHWkZICjNBWl8CVlxRSxpHUQFdXg0MDE1JXwBBRw1URysbFFQSDG5TVFYBCVFcVkoCAAUCUQsPUUgGAlIDA1RSV2kcRllBDThSAQsKBFgCVxtQB1sECwQFAk1UAl4GBQZSbQVuTlxlfGhSA35BbW9ed04CZwhUcApEUFUEQFt3CwRdDzEH"
key_hash = "n8lzyqvrq13riw707dmxhkzybrqqd1xkxpj0hpjh3gngs6va6lo859axo7pu9mvv"
user_email = "apexawsapex@outlook.jp"

meta_protected = True
encoded_email = base64.b64encode(user_email.encode('utf-8')).decode('utf-8')

w = encoded_email
g = key_hash
b = key_data

k = {}

def p(e, t):
    print(e)
    print(t)
    n = len(e)
    i = len(t)
    r = []
    for a in range(i):
        o = ord(t[a])
        s = ord(e[a % n])
        r.append(chr(o ^ s))
    return r

try:
    decoded_key_data = base64.b64decode(key_data).decode('utf-8')
    json_data = p(w+g+"76c065bbe09bdbf3663a28dd74a22bcb40dac7cc2386a2b7a4c69774ae1f461a", base64.b64decode(b).decode("utf-8"))
    combined_data = ''.join(json_data)
    combined_data = json.loads(combined_data)
    k = combined_data
    print(k)
except Exception as e:
    print("Error:", e)
    k = {}

n = {            "0": {
                "id": 374501,
                "original": 389512,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/1f53cfcccd0ac3b3fab76590c77be16c2e60be54.jpg"
            },
            "1": {
                "id": 374502,
                "original": 389513,
                "width": 4299,
                "height": 6071,
                "ident": "cover",
                "data": {},
                "filename": "contents/90963364d27ba9703a53ed520e20c91916158c0b.jpg"
            },
            "10": {
                "id": 374511,
                "original": 389522,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/028d7d5ce11c3c2b579ce5c538743b3a3b007006.jpg"
            },
            "11": {
                "id": 374512,
                "original": 389523,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/f7fea4a2fd4140a6884d3ad469e76d175caaa574.jpg"
            },
            "12": {
                "id": 374513,
                "original": 389524,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/3919ebcda59442d202f095bf1ffa6067af0bbe98.jpg"
            },
            "13": {
                "id": 374514,
                "original": 389525,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/32f2909a7556c29f1c3806e8268d8ce461c004c1.jpg"
            },
            "14": {
                "id": 374515,
                "original": 389526,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/8b2501707dbfaa20ec61e68d188c19c82c972416.jpg"
            },
            "15": {
                "id": 374516,
                "original": 389527,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/46d4db4960524b6bb0ea70ae6b59f11130390973.jpg"
            },
            "16": {
                "id": 374517,
                "original": 389528,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/bf7cd04b8f434fb6622900ee3cb71a6427f8af0d.jpg"
            },
            "17": {
                "id": 374518,
                "original": 389529,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/fc2dc4577ff4ed29a24c6e33d85c7917593cf9b5.jpg"
            },
            "18": {
                "id": 374519,
                "original": 389530,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/cbed2777b0b14cf5627c34bb8a281bccb2b54d64.jpg"
            },
            "19": {
                "id": 374520,
                "original": 389531,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/0d94041bab219d15a1cf07ef0293e20b70f320a4.jpg"
            },
            "2": {
                "id": 374503,
                "original": 389514,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/1479d4aca86e192e2eb808972d123b9fe043f3c5.jpg"
            },
            "20": {
                "id": 374521,
                "original": 389532,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/ddd68146c4fb3c3e1f5387b99071b14a660c91ea.jpg"
            },
            "21": {
                "id": 374522,
                "original": 389533,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/9bc5c63c44ed45883427a2816273a950a9bd3aa6.jpg"
            },
            "22": {
                "id": 374523,
                "original": 389534,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/47013e76d2325d6e28ba337dcd31f0585aa729fb.jpg"
            },
            "23": {
                "id": 374524,
                "original": 389535,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/60c8673a139b4c78e69a02bdabc1719a813ddcdd.jpg"
            },
            "24": {
                "id": 374525,
                "original": 389536,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/6b37fe9b63151a29aa3c4b2f3a2902d02b80a78c.jpg"
            },
            "25": {
                "id": 374526,
                "original": 389537,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/80663c67fe00f9041acf6608092c9b90c81aff6d.jpg"
            },
            "26": {
                "id": 374527,
                "original": 389538,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/66829ad43ba597d51de614e78ad104f9c03f7471.jpg"
            },
            "27": {
                "id": 374528,
                "original": 389539,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/9701b0b8be1729856204607427833a46254027ce.jpg"
            },
            "28": {
                "id": 374529,
                "original": 389540,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/bfcf3f3b742a8d69a08274a4a56fb796ec123c1e.jpg"
            },
            "29": {
                "id": 374530,
                "original": 389541,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/fd24189ec5b686c8d52110c1192434c922ee7b6e.jpg"
            },
            "3": {
                "id": 374504,
                "original": 389515,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/d1fa4468dd39ba050bc2f20619eadbe6d5609459.jpg"
            },
            "4": {
                "id": 374505,
                "original": 389516,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/2d8e53016ba1d4a16a602fbbb45be555822eff73.jpg"
            },
            "5": {
                "id": 374506,
                "original": 389517,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/4a9f47945d2a9622286b3a3add2efa2bb180bb31.jpg"
            },
            "6": {
                "id": 374507,
                "original": 389518,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/f9eae4ef82136af254492c6ed68bc31387b4f178.jpg"
            },
            "7": {
                "id": 374508,
                "original": 389519,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/93fdab4016e906efd9216655ff6d0e4d9305f6ee.jpg"
            },
            "8": {
                "id": 374509,
                "original": 389520,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/e3cb02a8720e77697fc0a237b907c3cf271ef779.jpg"
            },
            "9": {
                "id": 374510,
                "original": 389521,
                "width": 4299,
                "height": 6071,
                "ident": None,
                "data": {},
                "filename": "contents/38d128ffc2f8a59afafbed1bdd8a80d45487d475.jpg"
            }}
y = 128  # 任意の減算値（元のコードの `y`）

def D(e, t, n):
    i = t / n
    r = round(e / i)
    a = r / y
    o = (a - int(a)) < 0.15
    if o:
        r = a = round(a) * y
    else:
        a = math.ceil(a) * y
    return {
        "width": r,
        "height": n,
        "crop": o,
        "area": a * n
    }
    
def random_function():
    import random

    r = 48
    a = 1
    o = r
    s = [0] * r
    c = 0
    l = lambda x: random.random() if x is None else x

    for t in range(r):
        s[t] = l(None)

    def u():
        nonlocal o, a
        o += 1
        if o >= r:
            o = 0
        e = 1768863 * s[o] + 2.3283064365386963e-10 * a
        s[o] = e - (a := int(e))
        return s[o]

    def d(e):
        return int(e * (u() + 11102230246251565e-32 * (int(2097152 * u()) | 0)))

    def d_string(e):
        return ''.join(chr(33 + d(94)) for _ in range(e))

    def p(*args):
        nonlocal s
        for t in range(len(args)):
            for n in range(r):
                s[n] -= l(args[t])
                if s[n] < 0:
                    s[n] += 1

    def clean_string(e):
        e = e.strip().replace('\n ', '\n')
        return ''.join(c for c in e if not (0 <= ord(c) <= 31))

    def hash_string(e):
        nonlocal c
        e = clean_string(e)
        l(e)
        for t in range(len(e)):
            c = ord(e[t])
            for n in range(r):
                s[n] -= l(c)
                if s[n] < 0:
                    s[n] += 1

    def seed(e=None):
        if e is None:
            e = random.random()
        if not isinstance(e, str):
            e = str(e) or ""
        init_state()
        hash_string(e)

    def add_entropy(*args):
        nonlocal c
        e = ''.join(str(arg) for arg in args)
        p(c + int(random.random() * 1000000) + e)

    def init_state():
        nonlocal a, o
        l()
        for t in range(r):
            s[t] = l(" ")
        a = 1
        o = r

    def done():
        nonlocal l
        l = None

    def range_func(e):
        return d(e)

    def random_func():
        return d(float('inf') - 1) / float('inf')

    def float_between(e, t):
        return random_func() * (t - e) + e

    def int_between(e, t):
        return int(random_func() * (t - e + 1)) + e

    d.clean_string = clean_string
    d.hash_string = hash_string
    d.seed = seed
    d.add_entropy = add_entropy
    d.init_state = init_state
    d.done = done
    d.range = range_func
    d.random = random_func
    d.float_between = float_between
    d.int_between = int_between

    return d

    
class y_fun:
    def g(e, t):
        from random import random as r
        n = random_function()(t)
        i = len(e)
        a = 0
        o = 0
        s = e[:]
        while i:
            o = s[a := int(r() * i)]
            s[a] = s[i - 1]
            s[i - 1] = o
            i -= 1
        return s
    
    def u(e):
        return list(range(e))

def map_function(e, t, o, M, a, i, s):
    n = e % o
    r = (e - n) / o
    c = t % o
    l = (t - c) / o
    u = (l == s - 1) if i else (c == o - 1)  # 条件に応じて u を判定
    c *= M; # c に M を掛ける
    l *= M; # l に M を掛ける
    
    if (u):
        # u が true の場合の調整
        c -= 0 if i else a
        l -= a if i else 0
    
    # 結果をオブジェクトとして返す
    temp_json= {}
    temp_json["sx"] = n * M
    temp_json["sy"] = r * M
    temp_json["dx"] = c
    temp_json["dy"] = l
    return temp_json

# メイン処理
for key in k:
    A = n[key]  # `n[_]` を取得
    C = k[key]  # `k[_]` を取得
    P = C[2]
    L = C[0] ^ P
    M = C[1] ^ P
    I = math.floor(max(L, M) / y) * y

    # 条件付きループ
    while I > 0:
        z = D(min(L, M), max(L, M), I)
        if z['area'] < 3000000:
            break
        I -= y

    # 結果の格納
    if A:
        A['width'] = L if L < M else z['width']
        A['height'] = M if L < M else z['height']
        A['seed'] = P

def generate_fucking_idiot_shit(seed):
    # 実行例
    o = 11
    s = 15
    result = y_fun.g(y_fun.u(o * s), seed)
    return result  # ランダムに並べ替えられた結果が出力される
    

# 結果の確認
#print(n)
print("0 seed: "+str(n["0"]["seed"]))
result_seed = generate_fucking_idiot_shit(n["0"]["seed"])
#print(result_seed)
#e = 画像の場所

result_seed = [
  87,
  141,
  148,
  3,
  134,
  140,
  105,
  39,
  122,
  33,
  92,
  47,
  151,
  38,
  28,
  55,
  15,
  2,
  49,
  118,
  34,
  31,
  14,
  104,
  153,
  77,
  128,
  125,
  99,
  9,
  29,
  58,
  10,
  32,
  101,
  11,
  35,
  129,
  12,
  37,
  138,
  13,
  163,
  8,
  36,
  4,
  16,
  111,
  51,
  17,
  53,
  89,
  18,
  102,
  5,
  19,
  59,
  95,
  133,
  157,
  121,
  113,
  65,
  6,
  130,
  1,
  7,
  75,
  27,
  20,
  131,
  107,
  21,
  137,
  71,
  120,
  48,
  115,
  22,
  50,
  117,
  23,
  52,
  150,
  24,
  54,
  126,
  25,
  56,
  85,
  26,
  57,
  30,
  123,
  60,
  94,
  83,
  62,
  160,
  132,
  124,
  100,
  135,
  127,
  142,
  91,
  68,
  145,
  93,
  136,
  109,
  96,
  139,
  154,
  98,
  73,
  97,
  144,
  61,
  40,
  147,
  63,
  41,
  80,
  64,
  42,
  156,
  66,
  43,
  159,
  67,
  44,
  162,
  69,
  45,
  88,
  70,
  46,
  90,
  72,
  143,
  74,
  103,
  146,
  76,
  106,
  149,
  78,
  108,
  152,
  79,
  110,
  155,
  81,
  112,
  158,
  82,
  114,
  161,
  84,
  116,
  164,
  86,
  119,
  0
]

result_seed_fuck = [
    map_function(e=0, t=t, o=11, M=128, a=49, i=False, s=15) 
    for t in result_seed
]
print(result_seed_fuck)

#result_seed_fuck = map_function(e=0, t=result_seed, o=11, M=128, a=49, i=False, s=15)
#for i in json.loads(n):
#    print(i)