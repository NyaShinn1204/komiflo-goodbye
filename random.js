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

r_t = function(e) {
    return function() {
        var t, n, r = 48,
            a = 1,
            o = r,
            s = new Array(r),
            c = 0,
            l = new i;
        for (t = 0; t < r; t++) s[t] = l(Math.random());
        var u = function() {
                ++o >= r && (o = 0);
                var e = 1768863 * s[o] + 2.3283064365386963e-10 * a;
                return s[o] = e - (a = 0 | e)
            },
            d = function(e) {
                return Math.floor(e * (u() + 11102230246251565e-32 * (2097152 * u() |
                    0)))
            };
        d.string = function(e) {
            var t, n = "";
            for (t = 0; t < e; t++) n += String.fromCharCode(33 + d(94));
            return n
        };
        var p = function() {
            var e = Array.prototype.slice.call(arguments);
            for (t = 0; t < e.length; t++)
                for (n = 0; n < r; n++) s[n] -= l(e[t]), s[n] < 0 && (s[n] += 1)
        };
        return d.cleanString = function(e) {
            return e = (e = (e = e.replace(/(^\s*)|(\s*$)/gi, "")).replace(
                /[\x00-\x1F]/gi, "")).replace(/\n /, "\n")
        }, d.hashString = function(e) {
            for (e = d.cleanString(e), l(e), t = 0; t < e.length; t++)
                for (c = e.charCodeAt(t), n = 0; n < r; n++) s[n] -= l(c), s[n] < 0 &&
                    (s[n] += 1)
        }, d.seed = function(e) {
            null == e && (e = Math.random()), "string" != typeof e && (e = JSON.stringify(
                e) || ""), d.initState(), d.hashString(e)
        }, d.initState = function() {
            for (l(), t = 0; t < r; t++) s[t] = l(" ");
            a = 1, o = r
        }, void 0 !== e && d.seed(e), d.range = function(e) {
            return d(e)
        }, d.random = function() {
            return d(Number.MAX_VALUE - 1) / Number.MAX_VALUE
        }, d
    }()
};

function g(e, t) {
    for (var n = r_t(t), i = e.length, a = 0, o = 0, s = e.slice(0); i;)
        o = s[a = ~~(n.random() * i--)],
        s[a] = s[i], s[i] = o;
    return s
}

seed = 12257281
y_h = (h(11*15))
console.log(y_h)
var test_map = g(y_h, seed)
//test_map = 
console.log("map:", JSON.stringify(test_map, null ,2))


e = 0
t = {
    "color": "#fcfcfc",
    "data": {},
    "edges": {
      "left": 15921906,
      "right": 15921906,
      "top": 15921906,
      "bottom": 15921906,
      "hor": 15921906
    },
    "filename": "contents/1f53cfcccd0ac3b3fab76590c77be16c2e60be54.jpg",
    "height": 1920,
    "id": 374501,
    "ident": null,
    "image": "https://cdn.komiflo.com/scrambled/contents/1f53cfcccd0ac3b3fab76590c77be16c2e60be54",
    "index": 0,
    "naturalSpread": false,
    "original": 389512,
    "page": 1,
    "seed": 12257281,
    "spread": 1,
    "thumb": "https://cdn.komiflo.com/resized/396_desktop_medium_2x/contents/1f53cfcccd0ac3b3fab76590c77be16c2e60be54.jpg",
    "width": 1359
  }
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