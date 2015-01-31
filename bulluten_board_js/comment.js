// ---- 使用方法 -----
// html側で表示・非表示させたいものにidを設定する。
// 表示非表示切り替えるボタンに以下のソースを書く。
// <input ....  onclick="change_comment(id)" ... >
// (idには表示切り替えをしたいブロックのidを引数に)
// -------------------

var change_comment = function(id) {
    var is_display = document.getElementById(id).style.display;
    if (is_display == "") {
        document.getElementById(id).style.display = "none";
    } else {
        document.getElementById(id).style.display = "";
    }
}

