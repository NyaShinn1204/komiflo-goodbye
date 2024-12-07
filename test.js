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
i = false
M = 128  


var n = e % o; // e の o での余り
var r = (e - n) / o; // e を o で割った商
var c = t % o; // t の o での余り
var l = (t - c) / o; // t を o で割った商
var u = i ? (l === s - 1) : (c === o - 1); // 条件に応じて u を判定

c *= M; // c に M を掛ける
l *= M; // l に M を掛ける

console.log(u)
if (u) {
    // u が true の場合の調整
    c -= i ? 0 : a;
    l -= i ? a : 0;
}

// 結果をオブジェクトとして返す
result = {
    sx: n *= M, // n に M を掛けた値
    sy: r *= M, // r に M を掛けた値
    dx: c, // 調整後の c
    dy: l  // 調整後の l
};

console.log(JSON.stringify(result, null, 2));