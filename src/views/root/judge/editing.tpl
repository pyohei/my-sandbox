<h2>ジャッジ編集画面</h2>
<form action="/judge/update" method="post">
<input type="hidden" name="func" value="judge">
% profile = main_contents["profiles"][0]
  <table border="0" cellspacing="1">
    <tr>
      <th>
        ジャッジ名字:
      </th>
      <td>
        <input type="text" name="judge_first_name" size="10"
        value='{{profile["judge_first_name"]}}'>
      </td>
    </tr>
    <tr>
      <th>
        ジャッジ名前:
      </th>
      <td>
        <input type="text" name="judge_last_name" size="10"
        value='{{profile["judge_last_name"]}}'>
      </td>
    </tr>
    <tr>
      <th>
        ニックネーム:
      </th>
      <td>
        <input type="text" name="judge_nickname" size="10"
        value='{{profile["judge_nickname"]}}'>
      </td>
    </tr>
    <tr>
      <th>
        ジャッジ能力:
      </th>
      <td>
        <select name="judge_capacity">
          % degrees = {
          %     "0": "初",
          %     "1": "1",
          %     "2": "2",
          %     "3": "3",
          %     "4": "4",
          %     "5": "5",
          %     "6": "6",
          %     "7": "7",
          %     "8": "8",
          %     "": "???",
          %     }
          % for key in degrees.keys():
          %     if key == profile["judge_capacity"]:
          <option value='{{key}}' selected>{{degrees[key]}}</option>
          %     end
          %     if key != profile["judge_capacity"]:
          <option value='{{key}}'>{{degrees[key]}}</option>
          %     end
          % end
        </select>
      </td>
    </tr>
    <tr>
      <th>
        アドレス:
      </th>
      <td>
        <input type="text" name="email" size="30"
         value='{{profile["email"]}}'>
      </td>
    </tr>
    <tr>
      <th>
        登録日時
      </th>
      <td>
        {{profile["register_time"]}}
      </td>
    </tr>
    <tr>
      <th>
        最終更新日時
      </th>
      <td>
        {{profile["update_time"]}}
      </td>
    </tr>
  </table>
      <input type="submit" value="編集完了">
      <input type="reset" value="リセット">
</form>
