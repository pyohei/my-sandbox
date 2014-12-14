

var insert_score = function(type, score) {
    alert("ok");
    element = document.getElementById("technicalmerit");
    var cur_score = element.innerHTML;
    alert(cur_score);
    if
    if (cur_score == "" ) {
        alert("first");
        cur_score = score + ".";
        element.innerHTML = cur_score;
    } else {
        cur_score = cur_score + score;
        element.innerHTML = cur_score;
    }
}


var next = function () {
    var check =

