<h2>選手登録画面</h2>
<form action="/management/result" method="post">
<input type="hidden" name="func" value="contest">
  大会名:
    <input type="text" name="contest_name" size="10"><br>
  大会属性:
    <select name="contest_type">
      <option value="0">学生</option>
      <option value="1">選手権</option>
      <option value="">???</option>
    </select><br>
  採点方法:
    <select name="judge_type">
      <option value="0">OBO</option>
      <option value="1">CoP</option>
      <option value="2">オリジナル</option>
      <option value="">??</option>
    </select><br>
  大会日(入力例：2014-01-02):
    <input type="text" name="contest_date" size="10"><br>
  <input type="submit" value="登録"><br>
  <input type="reset" value="リセット">
</form>
