function loader () {
  var ob = new Object();
  ob.request = window.XMLHttpRequest;

  var xobj = new ob.request();

  xobj.open("GET", "http://google.com", true);
  xobj.send(null);
  alert(xobj.responseText);
  alert(xobj.readyState);
  alert(xobj.status);
}

function knowName () {
    var nameList = document.getElementsByName("selectName");
    document.writeln(nameList[1].value);
}

//document.writeln(ob.request);

/*
window.onbeforeunload = function (event) {
    event = event || window.event;
    if (event) {
        event.returnValue = "確認しましたか";
    } 

    // safari have to use below code.
    return "are you ok?";
}
*/
