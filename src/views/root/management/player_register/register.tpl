<h2>選手登録画面</h2>
<form action="/management/result" method="post">
<input type="hidden" name="func" value="player">
  選手名:
    <input type="text" name="player_name" size="10"><br>
  ニックネーム:
    <input type="text" name="player_nickname" size="10"><br>
  級:
    <select name="degree">
      <option value="0">初</option>
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
      <option value="7">7</option>
      <option value="8">8</option>
      <option value="">???</option>
    </select><br>
  国:
    <select name="country">
      <option value="0">日本</option>
    </select><br>
  タイプ:
    <input type="text" name="player_type" size="10"><br>
  大学名(学生の場合):
    <input type="text" name="college_name" size="10"><br>
  <input type="submit" value="登録"><br>
  <input type="reset" value="リセット">
</form>
