    <iframe width="420"
      height="315"
      src='{{main_contents["url"]}}'
      frameborder="0" allowfullscreen>
    </iframe>
% if main_contents["is_end"]:
<form action="/judge/result" method="post">
% end
% if not main_contents["is_end"]:
<form action="/judge/test" method="post">
% end
  テクニカルメリット:
    <select name="technical_merit_first">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select>
    .
    <select name="technical_merit_second">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select>
    <br>
  プレゼンテーション:
    <select name="presentation_first">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select>
    .
    <select name="presentation_second">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
    </select><br>
  <input type="submit" value="次へ">
</form>
