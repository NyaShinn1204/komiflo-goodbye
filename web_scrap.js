function h(e) {
    for (var t = [], n = 0; n < e; ++n) t.push(n);
    return t
}

i = function() {
    var e = 4022871197;
    return function(t) {
        if (t) {
            t = t.toString();
            for (var n = 0; n < t.length; n++) {
                var i = .02519603282416938 * (e += t.charCodeAt(n));
                i -= e = i >>> 0, e = (i *= e) >>> 0, e += 4294967296 * (i -= e)
            }
            return 2.3283064365386963e-10 * (e >>> 0)
        }
        e = 4022871197
    }
},

// 乱数生成器 'r_t'
r_t = function(seed) {
    return function() {
        var t, n;
        var poolSize = 48,                 // プールのサイズ
            a = 1,                         // 計算に使用される変数
            index = poolSize,              // プール内のインデックス
            pool = new Array(poolSize),    // 乱数のプール
            c = 0,                         // カウンター
            l = new i();                   // ハッシュ関数または乱数生成に使われるインスタンス

        // プールを初期化
        for (t = 0; t < poolSize; t++) {
            pool[t] = l(Math.random());
        }

        // ランダムな値を生成する関数 'u'
        var u = function() { // 165
            ++index;
            if (index >= poolSize) index = 0;
            var e = 1768863 * pool[index] + 2.3283064365386963e-10 * a;
            a = e | 0;             // 'e' の整数部分を取得
            pool[index] = e - a;   // 'e' の小数部分をプールに格納
            return pool[index];
        };

        // 'u' の出力を指定された範囲にスケーリングする関数 'd'
        var d = function(range) {
            return Math.floor(range * (u() + 1.1102230246251565e-16 * (2097152 * u() | 0)));
        };

        // 文字列をクリーンアップする関数
        d.cleanString = function(str) {
            str = str.replace(/(^\s*)|(\s*$)/gi, "");    // 前後の空白を削除
            str = str.replace(/[\x00-\x1F]/gi, "");      // 制御文字を削除
            str = str.replace(/\n /, "\n");              // 改行後の空白を削除
            return str;
        };

        // 文字列をハッシュし、内部状態を変更する関数
        d.hashString = function(str) {
            str = d.cleanString(str);
            console.log(str)
            str_log = l(str);
            console.log(str_log)
            for (t = 0; t < str.length; t++) {
                c = str.charCodeAt(t);
                for (n = 0; n < poolSize; n++) {
                    pool[n] -= l(c);
                    if (pool[n] < 0) pool[n] += 1;
                }
            }
        };

        // 乱数生成器をシードする関数
        d.seed = function(seedValue) {
            if (seedValue == null) seedValue = Math.random();
            if (typeof seedValue !== "string") seedValue = JSON.stringify(seedValue) || "";
            console.log("d.seed seedvalue", seedValue)
            d.initState();
            d.hashString(seedValue);
        };

        // 内部状態を初期化する関数
        d.initState = function() {
            l();
            for (t = 0; t < poolSize; t++) {
                pool[t] = l(" ");
            }
            a = 1;
            index = poolSize;
        };

        // シードが指定されていれば乱数生成器をシード
        if (seed !== undefined) {
            d.seed(seed);
        }

        // メソッドを公開
        d.range = function(max) {
            return d(max);
        };

        d.random = function() {
            return d(Number.MAX_VALUE - 1) / Number.MAX_VALUE;
        };

        return d;
    }();
};

function g(e, t) {
    for (var n = r_t(t), i = e.length, a = 0, o = 0, s = e.slice(0); i;) // ここでeのlength(165) loop
        o = s[a = ~~(n.random() * i--)],
        s[a] = s[i], s[i] = o;
    return s
}

seed = 12257281
y_h = (h(11*15))
console.log(y_h)
var test_map = g(y_h, seed)
console.log("map:", JSON.stringify(test_map, null ,null))
//test_map = 
//console.log("map:", JSON.stringify(test_map, null ,2))


e = 0
o = 11
a = 49
i = false
M = 128  

ops = test_map.map((function(e, t) {
    //console.log(y.h) // ここで11x15 x ページ数run
    var n = e % o
    var r = (e - n) / o
    var c = t % o
    var l = (t - c) / o
    var u = i ? l === s - 1 : c === o - 1;

    c *= M; // c に M を掛ける
    l *= M; // l に M を掛ける
    
    if (u) {
        // u が true の場合の調整
        c -= i ? 0 : a;
        l -= i ? a : 0;
    }
    
    // 結果をオブジェクトとして返す
    return {
        sx: n *= M, // n に M を掛けた値
        sy: r *= M, // r に M を掛けた値
        dx: c, // 調整後の c
        dy: l  // 調整後の l
    };
}))
console.log("ops: " + JSON.stringify(ops, null, 2));