<script type="text/javascript" src="/js/contest/register.js"></script>
<form name="contest_register" method="post"
  action="/contest/register">
  <input type="hidden" id="link_num" value="1">
  <h2>大会登録</h2>
  <p>大会名<input type="text" name="contest_name"></p>
  <p>大会日時<input type="text" name="contest_date"></p>
  <p>（空なら登録日が入る）</p>
  <p>大会種別<input type="text" name="contest_type"></p>
  <p>採点方法<input type="text" name="judge_type"></p>
  <p>画像<input type="text" name="contest_image"></p>

  <h2>動画登録</h2>
    <div id="input">
      <h3>動画番1</h3>
      <p>動画リンク<input type="text" id="1" name="movie_link1"></p>
      <p>開始秒<input type="text" name="start_time1"></p>
      <p>終了秒<input type="text" name="end_time1"></p>
      <p>滑走者<input type="text" name="player1"></p>
    </div>
  <p><input type="button" onclick="add_link_form()" value="追加"></p>

  <input type="submit" value="登録確認">
</form>
<h3>動画の登録に関して</h3>
<ul>
  <li>動画は最低3本登録が必要</li>
  <li>動画はそれぞれ説明が必要</li>
  <li>動画は管理者の承認が必要</li>
</ul>
