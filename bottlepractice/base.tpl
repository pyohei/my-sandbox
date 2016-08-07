<html>
<head>
  <title>{{title or 'No title'}}</title>
</head>
<body>
  <ul>
    % for b in base:
        <li>{{b}}</li>
    % end
  </ul>
% include('base_inherite.tpl', lists=['hello','world','!!!'])
% include('base_inherite2.tpl', lists=['HELLO','world','!!!'])
</body>
</body>
</html>

