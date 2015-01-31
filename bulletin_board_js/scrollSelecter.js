var add = function () {

    var visible = function (value) {
        var on = document.getElementById(value);
        on.style.display = 'block'
    };

    var selecter = document.getElementById("animal");
    for (var i=0; i < selecter.options.length; i++) {
        if (selecter.options[i].selected) {
            // alert(selecter.options[i].value);
            visible(selecter.options[i].value);
        };
    };

};

var mask = function (id) {
    var m = document.getElementById(id);
    m.style.display = 'none';
};
