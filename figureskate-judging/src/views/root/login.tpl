
<div id="explain">
  <h2>フィギュアスケートを採点しよう</h2>
</div>

<div id="user-sign-up">
  <fieldset class="category-group">
<!--
    <legend>ログイン</legend>
-->
    <form action="/menu" method="post">
      <table>
        <tr>
          <th>
            <label for="usern_id">User Id</label>
          </th>
          <td>
            <input type="text" name="user_id">
          </td>
        </tr>
        <tr>
          <th>
            <label for="password">Password</label>
          </th>
          <td>
            <input type="password" name="password">
          </td>
        </tr>
      </table>
      <div id="login_button">
        <input class="button-primary" type="submit" value="ログイン">
      </div>
    </form>
    <div id="forget_login">
      <a href="/forget">登録情報を忘れた</a>
    </div>
    新規ジャッジ登録は
    <div id="new_register">
      <a href="/register">
        <input type="button" class="button-primary" value="新規登録">
      </a>
    </div>
  </fieldset>
</div>
