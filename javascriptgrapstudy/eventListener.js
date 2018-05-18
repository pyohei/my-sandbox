var testButton = function () {
    // "window.event" calls active event
    // but mozilla doesn't use this.
    // alternatively, "arguments[0] can use
    var evt = window.event || arguments[0];
    // alert(evt);
    // srcElement is mainly used in IE
    // (but chrome and safari move)
    var src = evt.srcElement || evt.target;
    var name = src.id;
    alert("say!!");
};

/*
var eventTest = function () {
    
    var b = document.getElementById("eventButton");

    b.addEventListener("click", testButton, false);
};
*/

F = function () {};

var testEvent =  function () {
    var __getId = function (id) {
        return document.getElementById(id);
    };

    var __testButton = function () {
        // "window.event" calls active event
        // but mozilla doesn't use this.
        // alternatively, "arguments[0] can use
        var evt = window.event || arguments[0];
        // alert(evt);
        // srcElement is mainly used in IE
        // (but chrome and safari move)
        var src = evt.srcElement || evt.target;
        var name = src.id;
        alert("yaa!!");
    };

    var __switchComment = function () {
        var n = document.getElementsByName("selectName");
        alert(n);
        alert(n[0].selectedIndex);

        var selecter = document.formCheck.selectName;
        alert(selecter);
        var index = selecter.selectedIndex;
        for (var i = 0; i < selecter.length; i++) {
            var v = selecter.options[i].value;
            var ele = document.getElementById("response" + v);

            if (i == index) {
                ele.style.display = 'block';
            } else {
                alert("a");
                ele.style.display = 'none';
            };
        };
    };

    var setEvent = function () {
        var b = __getId("eventButton");
        b.addEventListener("click", __testButton, false);
        var myComment = document.formCheck.selectName;
        myComment.addEventListener("change", __switchComment, false);
    };


    setEvent();
};

window.addEventListener("load", testEvent, false);
