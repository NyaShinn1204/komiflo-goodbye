def map_function(e, t, o, M, a, i, s):
    ops = []
    for t, e in enumerate(t):
        n = e % o
        r = (e - n) // o
        c = t % o
        l = (t - c) // o
        u = (l == s - 1) if i else (c == o - 1)
    
        c *= M  # c に M を掛ける
        l *= M  # l に M を掛ける
    
        if u:
            # u が True の場合の調整
            c -= 0 if i else a
            l -= a if i else 0
    
        # 結果を辞書としてリストに追加
        ops.append({
            "sx": n * M,  # n に M を掛けた値
            "sy": r * M,  # r に M を掛けた値
            "dx": c,      # 調整後の c
            "dy": l       # 調整後の l
        })
        
    return ops
result_seed = []  # ここに0~164のシャッフルされたものを用意
# eは取得したいページの数(0からスタート)
# o = 11 (固定)
# a = 49 (固定)
# i = false (固定)
# M = 128  (固定)

# サンプル
result_seed = [52,13,144,145,41,95,11,56,44,72,47,14,6,97,49,116,65,156,87,115,77,133,136,121,1,9,161,83,152,60,130,141,17,155,30,113,63,137,70,36,5,40,22,159,68,64,89,114,73,94,111,31,158,146,105,34,8,7,93,43,29,99,122,123,76,164,139,119,18,148,92,86,35,19,138,91,163,151,0,88,98,59,54,79,50,75,84,10,2,23,45,3,157,162,110,90,61,42,107,21,126,33,4,37,26,140,71,80,124,74,24,134,27,38,82,103,62,51,20,32,28,104,25,48,96,69,131,55,129,118,150,109,154,160,117,132,143,127,81,67,149,100,153,53,78,125,142,101,58,66,16,120,112,102,128,85,57,39,147,106,12,46,135,15,108]
e = 0
o = 11
a = 49
i = False
M = 128 
s = 15

result_seed_fuck = map_function(e, result_seed, o, M, a, i, s)

print(result_seed_fuck)
