// Import the convertJsToPython function from your library
const { translateJSToPython } = require('convert-js2py');

// Define your JavaScript code that you want to convert
const jsCode = `
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

r_t = function(seed) {
    return function() {
        var t, n;
        var poolSize = 48,
            a = 1,
            index = poolSize,
            pool = new Array(poolSize),
            c = 0,
            l = new i();

        for (t = 0; t < poolSize; t++) {
            pool[t] = l(Math.random());
        }
        var u = function() {
            ++index;
            if (index >= poolSize) index = 0;
            var e = 1768863 * pool[index] + 2.3283064365386963e-10 * a;
            a = e | 0;
            pool[index] = e - a;
            return pool[index];
        };
        var d = function(range) {
            return Math.floor(range * (u() + 1.1102230246251565e-16 * (2097152 * u() | 0)));
        };
        d.cleanString = function(str) {
            str = str.replace(/(^\s*)|(\s*$)/gi, "");
            str = str.replace(/[\x00-\x1F]/gi, "");
            str = str.replace(/\n /, "\n");
            return str;
        };
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
        d.seed = function(seedValue) {
            if (seedValue == null) seedValue = Math.random();
            if (typeof seedValue !== "string") seedValue = JSON.stringify(seedValue) || "";
            console.log("d.seed seedvalue", seedValue)
            d.initState();
            d.hashString(seedValue);
        };
        d.initState = function() {
            l();
            for (t = 0; t < poolSize; t++) {
                pool[t] = l(" ");
            }
            a = 1;
            index = poolSize;
        };
        if (seed !== undefined) {
            d.seed(seed);
        }
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
    for (var n = r_t(t), i = e.length, a = 0, o = 0, s = e.slice(0); i;)
        o = s[a = ~~(n.random() * i--)],
        s[a] = s[i], s[i] = o;
    return s
}

seed = 12257281
y_h = (h(11*15))
console.log(y_h)
var test_map = g(y_h, seed)
console.log("map:", JSON.stringify(test_map, null ,null))

e = 0
o = 11
a = 49
i = false
M = 128  

ops = test_map.map((function(e, t) {
    var n = e % o
    var r = (e - n) / o
    var c = t % o
    var l = (t - c) / o
    var u = i ? l === s - 1 : c === o - 1;
    c *= M;
    l *= M;
    if (u) {
        c -= i ? 0 : a;
        l -= i ? a : 0;
    }
    return {
        sx: n *= M,
        sy: r *= M,
        dx: c,
        dy: l
    };
}))
console.log("ops: " + JSON.stringify(ops, null, 2));
`;

// Use the convertJsToPython function to convert the JavaScript code to Python
const pythonCode = translateJSToPython(jsCode);

// Print the generated Python code
console.log(pythonCode);