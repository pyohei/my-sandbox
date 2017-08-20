// 入力値から列を追加する
function createRow(tableName){
  // 入力値の取得
  var newId = document.addRow.newId.value;
  var newName = document.addRow.newName.value;

  // 入力値のチェック
  if (isInvalidInput(newId, newName)){
    alert("入力値に不正な値があります");
    return;
  }
  // 入力idとnameの取得
  var idNode = document.createTextNode(newId);
  var nameNode = document.createTextNode(newName);

  // テーブル要素の作成
  var tbodyElement = document.getElementById(tableName).getElementsByTagName("tbody")[0];
  var trElement = document.createElement("tr");
  var tdElement = document.createElement("td");
  var tdElement2 = document.createElement("td");
  var tdElement3 = document.createElement("td");
  var tdElement4 = document.createElement("td");

  // ボタン要素作成関数
  function generateButton(buttonName){

    var buttonElement = document.createElement("button");
    buttonElement.type = "button";
    var javascriptName = buttonName + "Row(this)";
    buttonElement.onclick = new Function(javascriptName);
    buttonElement.appendChild(document.createTextNode(buttonName));
    return buttonElement
  }

  // ボタン要素の追加
  var modifyButton = generateButton("modify");
  var deleteButton = generateButton("delete");

  // 子ノード作成(ここ微妙。。)
  tdElement.appendChild(idNode);
  tdElement2.appendChild(nameNode);
  tdElement3.appendChild(modifyButton);
  tdElement3.appendChild(deleteButton);
  trElement.appendChild(tdElement);
  trElement.appendChild(tdElement2);
  trElement.appendChild(tdElement3);
  tbodyElement.appendChild(trElement);
}

// 入力値チェック
function isInvalidInput(id, name){
  if (!id.match(/\S/g) || !name.match(/\S/g)){
    return true;    // この正規表現あんまり分かっていない。
  }
  idList = getNums(0);
  nameList = getNums(1);
  if (isContain(id, idList)){
    return true;
  }
  if (isContain(name, nameList)){
    return true;
  }
  if (!isFinite(id)){
    return true;
  }
  alert("ok!!")
  return false;
}

// 対象がリストに含まれるかどうかの確認
function isContain(target, compares){
  for (var i = 0; i < compares.length; i++){
    if(compares[i] === target){
      return true;
    }
  }
  return false;
}

// テーブルをソートする
function sortNum(rowNum){
  var numList = getNums(rowNum);
  var numList = collumnSort(rowNum, numList);
  arrange(numList);
}

// 列の値を取得する
function getNums(row){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  var sortIndex = [];
  for (var i in trList) {
    if (i == 0){
      continue;
    }
    if (isNaN(i)){    // 修正したいなー
      break;
    }
    sortIndex.push(trList[i].cells[row].firstChild.nodeValue);
  }
  return sortIndex;
}

// 列のソートをする
function collumnSort(rowNum, rows){
  var sortList = [];
  var num = 1;
  for (var r = 0; r < rows.length; r++) {
    var o = {};
    o["order"] = num;
    o["comp"] = rows[r];
    sortList.push(o);
    num = num + 1;
  }
  if (rowNum === 0){
    alert("aa");
    var results = sortList.sort(function (a, b){
      o = a['comp'];
      p = b['comp'];
      return a['comp'] - b['comp'];
    });
  }
  if (rowNum == 1){
    alert("bb");
    var results = sortList.sort(function (a, b) {
      var o, p;
      if (typeof a === 'object' && typeof b === 'object' && a && b) {
        o = a['comp'];
        p = b['comp'];
        if (o === p) {
          return 0;
        }
        if (typeof o === typeof p) {
          return o < p ? -1 : 1;
        }
        return typeof o < typeof p ? -1 : 1;
      }
    });
  }
  var exchangeList = [];
  for (var n = 0; n < results.length; n++){
    exchangeList.push(results[n]["order"]);
  }
  return exchangeList;
}

// テーブルの列を入れ替える
function arrange(orders){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  var header = trList[0].cloneNode(true);
  var clones = [];
  for (var i = 0; i < orders.length; i++) {
    clones.push(trList[orders[i]].cloneNode(true));
  }
  for (var i = 0; i < orders.length; i++){
    trList[i+1].parentNode.replaceChild(clones[i], trList[i+1]);
  }
}

// テーブル列の全削除
function deleteAll(){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  for (var i = 0; i <= trList.length; i ++){
    bodys.deleteRow(1);
  }
}

// 列の削除
function deleteRow(row){
  var n = row.parentNode.parentNode;
  n.parentNode.deleteRow(n.sectionRowIndex);
}

// 列の修正
function modifyRow(row){
  var n = row.parentNode.parentNode;
  id = window.prompt("new id is...?");
  name = window.prompt("new name is...?");
  // 入力値のチェック
  if (isInvalidInput(id, name)){
    alert("入力値に不正な値があります");
    return;
  }
  n.cells[0].innerText = id;
  n.cells[1].innerText = name;
}