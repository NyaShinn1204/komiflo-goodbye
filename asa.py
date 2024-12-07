import random
import math
import json
import re

# h関数
def h(e):
    return [n for n in range(e)]

# iクラス
class i:
    def __init__(self):
        self.e = 4022871197

    def __call__(self, t=None):
        if t:
            t = str(t)
            for char in t:
                self.e += ord(char)
                i = 0.02519603282416938 * self.e
                i -= self.e
                self.e = int(i) & 0xFFFFFFFF
                i *= self.e
                i -= self.e
                self.e = int(i) & 0xFFFFFFFF
            return 2.3283064365386963e-10 * (self.e & 0xFFFFFFFF)
        self.e = 4022871197

# r_t関数
def r_t(seed=None):
    def u(pool, index, a):
        index += 1
        if index >= len(pool):
            index = 0
        e = 1768863 * pool[index] + 2.3283064365386963e-10 * a
        a = int(e)  # Floats are truncated to ints
        pool[index] = e - a
        return pool[index], index, a

    def d(range, pool, index, a):
        # u(pool, index, a)[0]を整数にキャストしてからビット演算
        return math.floor(range * (int(u(pool, index, a)[0]) + 1.1102230246251565e-16 * (2097152 * int(u(pool, index, a)[0]) | 0)))

    class Random:
        def __init__(self, seed=None):
            self.pool_size = 48
            self.pool = [0] * self.pool_size
            self.index = self.pool_size
            self.a = 1
            self.l = i()
            if seed:
                self.seed(seed)
            else:
                self.seed(random.random())

        def seed(self, seed_value):
            if isinstance(seed_value, str):
                seed_value = json.dumps(seed_value)
            self.init_state()
            self.hash_string(seed_value)

        def init_state(self):
            self.pool = [self.l(" ")] * self.pool_size
            self.a = 1
            self.index = self.pool_size

        def hash_string(self, s):
            s = self.clean_string(s)
            for c in s:
                for n in range(self.pool_size):
                    self.pool[n] -= self.l(ord(c))
                    if self.pool[n] < 0:
                        self.pool[n] += 1

        def clean_string(self, s):
            # sが整数の場合は文字列に変換
            if isinstance(s, int):
                s = str(s)
            # 正規表現を使って前処理
            s = s.strip()
            s = re.sub(r'[\x00-\x1F]', '', s)
            s = s.replace("\n ", "\n")
            return s

        def random(self):
            return d(1.0, self.pool, self.index, self.a) / 1.0

        def range(self, max_val):
            return d(max_val, self.pool, self.index, self.a)

    return Random(seed)

# g関数（シャッフル）
def g(e, seed):
    r = r_t(seed)
    i = len(e)
    a = 0
    s = e[:]
    while i:
        idx = math.floor(r.random() * i)  # 正しいインデックスの選択
        o = s[a]  # シャッフル対象の要素
        s[a] = s[idx]  # 交換
        s[idx] = o  # 交換
        i -= 1
    return s

# メイン
seed = 12257281
y_h = h(11 * 15)
print("y_h:", y_h)
test_map = g(y_h, seed)  # シャッフルされたmap
print("map:", test_map)

o = 11
a = 49
i = False
M = 128

ops = []
for t, e in enumerate(test_map):
    n = e % o
    r = (e - n) // o
    c = t % o
    l = (t - c) // o
    u = i and (l == s - 1) or (c == o - 1)
    c *= M
    l *= M
    if u:
        c -= 0 if i else a
        l -= a if i else 0
    ops.append({
        "sx": n * M,
        "sy": r * M,
        "dx": c,
        "dy": l
    })

print("ops:", ops)
