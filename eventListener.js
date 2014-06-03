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
    alert(name)
        
    alert("say!!");
};

/*
var eventTest = function () {
    
    var b = document.getElementById("eventButton");

    b.addEventListener("click", testButton, false);
};
*/

F = function () {};

var ee =  function () {
    return {
        init: function () {
            window.addEventListener("load", this.eventTest, false);
        },
        eventTest: function () {
            /*
            // "window.event" calls active event
            // but mozilla doesn't use this.
            // alternatively, "arguments[0] can use
            var evt = window.event || arguments[0];
            // alert(evt);
            // srcElement is mainly used in IE
            // (but chrome and safari move)
            var src = evt.srcElement;
            alert(src.id);
            alert(evt.target.id);
            var name = src.id;
            alert(name)
            */

            var b = document.getElementById("eventButton");
            // var b = document.getElementById("eventButton");
            b.addEventListener("click", testButton, false);
            // b.addEventListener("click", testButton, false);
        }
    };
};

var tea = ee();
tea.init();

