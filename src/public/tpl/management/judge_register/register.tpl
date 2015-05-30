<h2>ジャッジ登録画面</h2>
<form action="/management/result" method="post">
<input type="hidden" name="func" value="judge">
  <table border="0" cellspacing="1">
    <tr>
      <th>
        ジャッジ名字:
      </th>
      <td>
        <input type="text" name="judge_first_name" size="10"><br>
      </td>
    </tr>
    <tr>
      <th>
        ジャッジ名前:
      </th>
      <td>
        <input type="text" name="judge_last_name" size="10"><br>
      </td>
    </tr>
    <tr>
      <th>
        ニックネーム:
      </th>
      <td>
        <input type="text" name="judge_nickname" size="10"><br>
      </td>
    </tr>
    <tr>
      <th>
        ジャッジ能力:
      </th>
      <td>
        <select name="judge_capacity">
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
      </td>
    </tr>
    <tr>
      <th>
        アドレス:
      </th>
      <td>
        <input type="text" name="email" size="10"><br>
      </td>
    </tr>
    <tr>
      <th>
        登録日(入力方式:"2013-01-03"):
      </th>
      <td>
        <input type="text" name="register_time" size="10"><br>
      </td>
    </tr>
    <tr>
      <th>
        パスワード:
      </th>
      <td>
        <input type="text" name="password_master" size="15"><br>
      </td>
    </tr>
    <tr>
      <th>
        パスワード（再入力）:
      </th>
      <td>
        <input type="text" name="password_standby" size="15"><br>
      </td>
    </tr>
  </table>
      <input type="submit" value="登録">
      <input type="reset" value="リセット">
</form>
