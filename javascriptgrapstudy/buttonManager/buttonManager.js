// Create at 2014.05.31
var hilight = function () {
    var h = document.getElementById('testbutton');
    h.style.cursor = 'pointer';
};

/* --- bad function ---
var setAlert = function () {
    var i; 
    for ( i = 1; i < 6; i++ ) {
        var id = document.getElementById("b" + String(i));
        id.onclick = function (i) {
            alert(i);
        };
    }
}
---*/

/* --- good function --- */
var setAlert = function () {
    var alerter = function (i) {
        return function (e) {
            alert(i);
        };
    };

    var i; 
    for ( i = 1; i < 6; i++ ) {
        var id = document.getElementById("b" + String(i));
        id.onclick = alerter(i);
    }
}

