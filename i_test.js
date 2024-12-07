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
}

var t, n;
var poolSize = 48,                 // プールのサイズ
    a = 1,                         // 計算に使用される変数
    index = poolSize,              // プール内のインデックス
    pool = new Array(poolSize),    // 乱数のプール
    c = 0,                         // カウンター
    l = new i();                   // ハッシュ関数または乱数生成に使われるインスタンス

l();
for (t = 0; t < 48; t++) {
    pool[t] = l(" ");
}

str = 12257281
console.log(str)
str_log = l(str);
console.log(str_log)