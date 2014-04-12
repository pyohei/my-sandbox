function createRow(id){
  var tbodyElement = document.getElementById(id).getElementsByTagName("tbody")[0];
  var trElement = document.createElement("tr");
  var tdElement = document.createElement("td");
  var tdElement2 = document.createElement("td");
  var contentNode = document.createTextNode(document.addRow.addValue.value);
  alert(contentNode);

  tdElement.appendChild(contentNode);
  tdElement2.appendChild(document.createTextNode("t"));
  trElement.appendChild(tdElement);
  trElement.appendChild(tdElement2);
  tbodyElement.appendChild(trElement);
}

function sortNum(rowNum){
  var numList = getNums(rowNum);
  var numList = numList.sort();
  alert(numList);
  // var numLists = document.getElementById("num");
  // var numList = numLists.getElementsByTagName("tr");
  // alert(numList.item(2).cells.item(0).firstChild.nodeValue);
  //var childList = numLists.childNodes;
  // alert(childList[1].innerHTML);
}

function getNums(row){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  var sortIndex = [];
  for (var i in trList) {
    // alert(i);
    if (i == 0){
      continue;
    }
    if (isNaN(i)){
      break;
    }
    // alert(trList[i].cells[row].firstChild.nodeValue);
    sortIndex.push(trList[i].cells[row].firstChild.nodeValue);
  }
  return sortIndex;
  // for (var trBody in trList) {
  //   alert(trBody.item(0));
  // }
//  alert(numList.item(2).cells.item(0).firstChild.nodeValue);
}

function sort(rows){
  return rows.sort();
}

/* http://d.hatena.ne.jp/sandai/20100823/p1#016 */