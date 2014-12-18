<script type="text/javascript" src="/js/contest/register.js"></script>

<form name="contest_register" method="post"
  action="/contest/register">
  <input type="hidden" id="link_num" value="1">
  <h2>大会登録</h2>
  <div id="contest_header">
    <table>
      <tr>
        <th>
          大会名<span class="must">必須</span>
        </th>
        <td><input type="text" name="contest_name"></td>
        <th>
          大会日時<span class="must">必須</span>
        </th>
        <td><input type="text" name="contest_date"></td>
      </tr>
      <tr>
        <th>
          大会種別<span class="must">必須</span>
        </th>
        <td>
          <select name="contest_type">
            <option value="1">選手権</option>
            <option value="2">学生</option>
          </select>
        <th>
          採点方法<span class="must">必須</span>
        </th>
        <td>
          <select name="judge_type">
            <option value="1">OBO</option>
            <option value="2">CoP</option>
          </select>
        </td>
      </tr>
      <tr>
        <th>画像<span class="option">任意</span></th>
        <td><input type="text" name="contest_image"></td>
      </tr>
    </table>
  </div>

  <h2>動画登録
    <input type="button" onclick="add_link_form()" value="追加">
    <input type="submit" value="登録確認">
  </h2>
  <div id="input"></div>
    <div id="contest_detail">
      <h3 id="title">動画1</h3>
      <table>
        <tr>
          <th>動画リンク<span class="must">必須</span></th>
          <td colspan="3">
            <input type="text" class="movie_link"
                   name="movie_link1"></td>
        </tr>
        <tr>
          <th>開始秒<span class="option">任意</span></th>
          <td><input type="text" name="start_time1"></td>
          <th>終了秒<span class="option">任意</span></th>
          <td><input type="text" name="end_time1"></td>
        </tr>
        <tr>
          <th>滑走者<span class="must">必須</span></th>
          <td><input type="text" name="player1"></td>
        </tr>
      </table>
    </div>

</form>
<h3>動画の登録に関して</h3>
<ul>
  <li>動画は最低3本登録が必要</li>
  <li>動画はそれぞれ説明が必要</li>
  <li>動画は管理者の承認が必要</li>
</ul>
