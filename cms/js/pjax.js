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

        // set path and method (default method is "POST")
        open: function (path, method) {
            if (!path) {
                return;
            }
            if (method === "GET") {
                var m = "GET";
            } else {
                var m = "POST";
            }
            alert(m);
            alert(path);
            pjax_obj.request.open(m, path);
        },

        // set header if need.
        set_header: function (header) {
            pjax_obj.request.setRequestHeader(
                "Content-Type", header);
        },

        //send request
        send: function () {
            pjax_obj.request.send("");
        }
    };
}

Pjax.prototype.alerter = function () {
    alert("a");
}

// test mode
var pjax_test = function () {
    var ins = function (a) {
        var r = document.getElementById("resp");
        r.value = a;
    }

    var pjax = Pjax();
    pjax.set(ins);
    pjax.open("./json", "POST");
    pjax.send();

}
