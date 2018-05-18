// Create at 2014.05.24
document.writeln("Hello World!");

/* ---- called from method ---- */
var myObject = {
    value: 0,
    increment: function (inc) {
        // alert(this);
        // this result: [object Object]
        this.value += typeof inc === 'number' ? inc :1;
    }
};

myObject.increment();
document.writeln(myObject.value);

myObject.increment(3);
document.writeln(myObject.value);

/* ---- called from function ---- */
// this usage of function is bad.
var glo = "a";
var add = function (a, b) {
    // alert(this);
    // this result : [object Window]
    //
    // for example, the following process changes valeu of glo.
    // but this variablity is in function add.
    // to avoid this change, write blow code.
    this.glo = "b"
    return a + b;
};
var sum = add(3, 4);
document.writeln(typeof sum);
document.writeln(glo);

// avoid this change
// add double method in myObject
myObject.double = function () {
    var that = this;    // avid value

    var helper = function () {
        that.value = add(that.value, that.value);
    };
    helper();
};
myObject.double();
document.writeln(myObject.value);


/* ---- called from constracter ---- */
var Quo = function (string) {
    this.status = string;
    // alert(this);
    // alert(status);
};

Quo.prototype.get_status = function () {
    return this.status;
};

// Quo("stri");
var myQuo = new Quo("confused");
document.writeln(myQuo);
// bad pattern
var yourQuo = Quo("confused");
document.writeln(myQuo.get_status());
// As this function is called from prototype,
// values don't change ???


/* ---- called from apply ---- */
var array = [3, 4];
var sum = add.apply(null, array);
document.writeln(sum);

var statusObject = {
    status: "SKATING!"
};

var status = Quo.prototype.get_status.apply(statusObject);

document.writeln(status);

/* ---- use argument function ---- */
var sum = function () {
    var i, sum = 0;
    for (i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    };
    return sum;
};

document.writeln(sum(4,2,4,2,3,4));

/* ---- check type of return ---- */
var RetOb = function () {
    var a = 2;
};

var retOb = new RetOb();
document.writeln(retOb);    // empty object

/* ---- prototype test ---- */
var stooge = {
    "first": "Hello!",
    "second": "BYE!",
    "third": "GOOD!!"
};

if (typeof Object.create !== 'function') {
    Object.create = function (o) {
        var F = function () {};
        F.prototype = o;
        return new F();
    };
}
var re_stooge = Object.create(stooge);
// inherit stooge object
document.writeln(re_stooge["first"]);


/* ---- extention of variable ---- */
Function.prototype.method = function (name, func) {
    this.prototype[name] = func;
    return this;
};

Number.method('integer', function () {
    return Math[this < 0 ? 'ceil' : 'floor'](this);
});

document.writeln((-10 / 3).integer() + '<br>');

/* ---- recursive function ---- */
var hanoi = function (disc, src, aux, dst) {
    if (disc > 0) {
        hanoi(disc - 1, src, dst, aux);
        document.writeln('Move disc ' + disc + ' from ' + 
            src + ' to ' + dst + '<br>');

        hanoi(disc - 1, aux, src, dst);
    }
};

hanoi(3, 'Src', 'Aux', 'Dst');

var quo = function (status) {
    return {
        get_status: function () {
            return status;
        }
    };
};

var firstQuo = quo("test");
var secondQuo = quo("TEST");

document.writeln(firstQuo.get_status());
document.writeln(secondQuo.get_status());

/* ---- object creater ---- */
if (typeof Object.create !== 'function') {
    Object.create = function (o) {
        var F = function () {};
        F.prototype = o;
        return new F();
    };
}

var myMammal = {
    name: 'Herb the Mammal',
    get_name: function () {
        return this.name;
    },
    says: function () {
        return this.saying || '';
    }
};

var myCat = Object.create(myMammal);
myCat.name = 'Henrietta';
myCat.saying = 'meow';
myCat.purr = function (n) {
    var i, s = '';
    for (i = 0; i < n; i++) {
        if (s) {
            s += '-';
        }
        s += 'r';
    }
    return s;
};

myCat.get_name = function () {
    return this.says() + ' ' + this.name + ' ' + this.says();
};

document.writeln(myCat.get_name());

var i;
var word;
var text = "I am Tom. I like music, " +
    "and I am musician. so, if possible " +
    "would you like to become a friend Constractor.";
var words = text.toLowerCase().split(/[\s,.]+/);
var count = {};
for (i = 0; i < words.length; i += 1) {
    word = words[i];
    if (count[word]) {
        count[word] += 1;
    } else {
        count[word] = 1;
    }
}

document.writeln(count.hasOwnProperty("i"));
