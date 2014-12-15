<script type="text/javascript" src="/js/contest/register.js"></script>

<form name="contest_register" method="post"
  action="/contest/register">
  <input type="hidden" id="link_num" value="1">
  <h2>大会登録</h2>
  <div id="contest_header">
    <ul>
      <li>大会名<input type="text" name="contest_name"></li>
      <li>大会日時(空なら当日)<input type="text" name="contest_date"></li>
      <li>大会種別<input type="text" name="contest_type"></li>
      <li>採点方法<input type="text" name="judge_type"></li>
      <li>画像<input type="text" name="contest_image"></li>
    </ul>
  </div>

  <h2>動画登録</h2>
  <p><input type="button" onclick="add_link_form()" value="追加"></p>
    <div id="input">
      <h3>動画番1</h3>
      <ul>
        <li>動画リンク
          <input type="text" id="1" name="movie_link1">
        </li>
        <li>開始秒<input type="text" name="start_time1"></li>
        <li>終了秒<input type="text" name="end_time1"></li>
        <li>滑走者<input type="text" name="player1"></li>
      </ul>
    </div>

  <input type="submit" value="登録確認">
</form>
<h3>動画の登録に関して</h3>
<ul>
  <li>動画は最低3本登録が必要</li>
  <li>動画はそれぞれ説明が必要</li>
  <li>動画は管理者の承認が必要</li>
</ul>
