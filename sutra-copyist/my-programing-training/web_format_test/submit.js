// submit時の機能をオブジェクトでまとめておく
var functions = {
    "insert": "bbb.b.bbb.bbbb",
    "update": "xxx.xxxx.xxx.xxx",
    "delete": "yyy.yyyy.yyyy.yyy",
    "import": "zzzz.zzz.zzzz.zzz",
    "export": "aaaa.aaaa.aaaa.aa"
}

// funcのvalueに属性を入れてsubmitする
var submit_comment = function(func) {
    var elements = document.getElementsByName("func");
    elements[0].value = functions[func];
    is_submit();
    document.main.submit();
}

