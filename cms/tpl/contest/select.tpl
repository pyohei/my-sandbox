<script type="text/javascript" src="/js/contest/select.js"></script>

<h2>大会選択</h2>
<form method="post" name="main" action="/judge/judging">
<input type="hidden" name="contest_no" value="">
  <div id="menue_selecter">
    <ul>
      % for contest in main_contents["contests"]:
        <li>
          <a href="#"
             onclick="select_contest({{contest['contest_no']}})">
             {{contest["contest_name"]}}
          </a>
        </li>
      % end
    </ul>
  </div>
</form>
