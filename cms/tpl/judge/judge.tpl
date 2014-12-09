
<script language="javascript">
<!--

var insert_score = function(type, score) {
  element = document.getElementById("technicalmerit");
  var cur_score = element.innerHTML;
  alert(cur_score);
  if (cur_score == "" ) {
    alert("first");
  }
}

-->
</script>

<div id="movie_frame">
  <iframe id="movie_iframe" width="640" height="400" src='{{main_contents["url"]}}'
      frameborder="0" >
  </iframe>
</div>
% if main_contents["is_end"]:
<form action="/judge/result" method="post">
% end
% if not main_contents["is_end"]:
<form action="/judge/test" method="post">
% end
<div id="score_boards">
  <div class="score_board">
    <ul>
      <li><a href="#" onclick-"insert_score(1, 7)">7</a></li>
      <li><a href="#" >8</a></li>
      <li><a href="#" >9</a></li>
      <li><a href="#" >4</a></li>
      <li><a href="#" >5</a></li>
      <li><a href="#" >6</a></li>
      <li><a href="#" >1</a></li>
      <li><a href="#" >2</a></li>
      <li><a href="#" >3</a></li>
      <li><a href="#" >0</a></li>
      <li><a href="#" ></a></li>
      <li><a href="#" >C</a></li>
    </ul>
  </div>
  <div class="score_board">
    <ul>
      <li><a href="#" >0</a></li>
      <li><a href="#" ></a></li>
      <li><a href="#" ></a></li>
      <li><a href="#" >1</a></li>
      <li><a href="#" >2</a></li>
      <li><a href="#" >3</a></li>
      <li><a href="#" >4</a></li>
      <li><a href="#" >5</a></li>
      <li><a href="#" >6</a></li>
      <li><a href="#" >7</a></li>
      <li><a href="#" >8</a></li>
      <li><a href="#" >9</a></li>
    </ul>
  </div>
</div>
<input type="button" onclick="insert_score(1,7)" value="test">>
<div id="technicalmerit"></div>

  <!-- これは仮の処置 -->
  <br><br>
  <div class="score">
    テクニカルメリット:
      <select name="technical_merit_first">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
      </select>
      .
      <select name="technical_merit_second">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
      </select>
  </div>
  <div class="score">
  プレゼンテーション:
    <select name="presentation_first">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select>
    .
    <select name="presentation_second">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select><br>
  </div>
  <input type="submit" value="次へ">
</form>
