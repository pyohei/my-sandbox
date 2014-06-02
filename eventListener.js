var testButton = function () {
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
            var b = document.getElementById("eventButton");
            b.addEventListener("click", testButton, false);
        }
    };
};

var tea = ee();
tea.init();

