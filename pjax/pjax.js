// Ajax handler
//
// *** how to use ***
//   var pjax = Pjax();
//   pjax.set(func); // func is function you wnat to execute
//   pjax.open();
//   pjax.send();


// main frame
var Pjax = function () {
    // check variable pjax_obj
    if (typeof pjax_obj == "undefined") {
        var pjax_obj = new Object();
    }

    pjax_obj.request = new XMLHttpRequest();
    
    return {
        set: function (func) {
            pjax_obj.request.onreadystatechange = function () {
                if (pjax_obj.request.readyState == 4) {
                    func(pjax_obj.request.responseText);
                }
            }
        },

        open: function () {
            pjax_obj.request.open("POST", "/json");
        },

        send: function () {
            pjax_obj.request.send("");
        }
    };
}


// test mode 
var pjax_test = function () {
    var ins = function (a) {
        var r = document.getElementById("resp");
        r.value = a;
    }

    var pjax = Pjax();
    pjax.set(ins);
    pjax.open();
    pjax.send();

}
