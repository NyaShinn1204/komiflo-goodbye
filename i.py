def i():
    e = 4022871197

    def inner(t=None):
        nonlocal e
        if t:
            t = str(t)
            for n in range(len(t)):
                e += ord(t[n])
                i_val = 0.02519603282416938 * e

                # JavaScriptのビット演算を再現
                e = int(i_val) & 0xFFFFFFFF  # e = i >>> 0
                i_val -= e

                i_val *= e
                e = int(i_val) & 0xFFFFFFFF  # e = i >>> 0

                i_val -= e
                e += 4294967296 * i_val
            return 2.3283064365386963e-10 * (e & 0xFFFFFFFF)
        else:
            e = 4022871197

    return inner

# 変数の初期化
t = None
n = None
poolSize = 48       # プールのサイズ
a = 1               # 計算に使用される変数
index = poolSize    # プール内のインデックス
pool = [0] * poolSize  # 乱数のプール
c = 0               # カウンター

l = i()  # ハッシュ関数または乱数生成に使われるインスタンス

l()  # eを初期化

for t in range(48):
    pool[t] = l(" ")

str = 12257281
print(str)
str_log = l(str)
print(str_log)