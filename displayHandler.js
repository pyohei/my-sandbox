var changeRow = function () {
    var allOn = function () {
        var t = document.getElementsByName("animal");
        alert(t.length);
        for (var n=0; n < t.length; n++) {
            t[n].style.display = '';
        };
    };
    allOn();
    var myList = {
        "like": ["dog"],
        "hate": ["monkey"],
        "normal": ["cat", "bird"]
    };
    var sele = document.getElementById("selecter");
    var i = sele.selectedIndex;
    var selValue = sele.options[i].value;
    for (var i=0; i < myList[selValue].length; i++) {
        var hideId = myList[selValue][i];
        alert(hideId);
        document.getElementById(hideId).style.display = "none";
    };
};
