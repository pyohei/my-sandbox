<h2>結果</h2>

<h3>{{main_contents["contest_name"]}}</h3>
% for n, score in enumerate(main_contents["rank"]):
  % if n == 0:
  <div id="gold">
  % end
  % if n == 1:
  <div id="silver">
  % end
  % if n not in (0, 1):
  <div id="bronze">
  % end
    <span>{{n+1}}位</span>
    <span>{{score["player_name"]}}</span>
  </div>
% end
