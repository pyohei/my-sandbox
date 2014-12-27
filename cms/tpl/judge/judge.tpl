
<script type="text/javascript" src="/js/judge/judge.js"></script>

<div id="judge_frame">
  <div id="movie_frame">
    <iframe id="movie_iframe" width="480" height="320" src='{{main_contents["url"]}}'
        frameborder="0" >
    </iframe>
  </div>
  % if main_contents["is_end"]:
  <form action="/judge/result" method="post">
  % end
  % if not main_contents["is_end"]:
  <form action="/judge/judging" method="post">
  <input type="hidden" name="player_no" value="1">
  % end
    <div class="score">
      <p>テクニカルメリット<p>
        <div class="point">
          <select name="technical_merit_first">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
          </select>
          .
          <select name="technical_merit_second">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
          </select>
        </div>
      <p>プレゼンテーション</p>
        <div class="point">
          <select name="presentation_first">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
          </select>
          .
          <select name="presentation_second">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
          </select>
      </div>
    <input type="button" value="Next" onclick="next()">
  </form>
</div>
