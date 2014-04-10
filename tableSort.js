function createRow(id){
  var tbodyElement = document.getElementById(id).getElementsByTagName("tbody")[0];
  var trElement = document.createElement("tr");
  var tdElement = document.createElement("td");
  var contentNode = document.createTextNode(document.addRow.addValue.value);

  tdElement.appendChild(contentNode);
  trElement.appendChild(tdElement);
  tbodyElement.appendChild(trElement);
}

function sortNum(){
  var numLists = document.getElementById("num");
  var childList = numLists.childNodes;
  alert(childList[1].innerHTML);
}

/* http://d.hatena.ne.jp/sandai/20100823/p1#016 */