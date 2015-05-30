// contest movei add
function add_link_form() {
    movie_form.add();
};

var movie_form = {
    add: function() {
        this._add_link();
    },
    _add_link: function() {
        var number = {
            __count: function() {
                var count = document.getElementById("link_num").value;
                return parseInt(count, 10) + 1;
            },
            __add: function(id) {
                document.getElementById("link_num").value = id;
            },
        };

        var links = {
            append_top: function(id, tag) {
                e = document.getElementById(id);
                e.insertBefore(tag, e.firstChild)
            },
            __create_tag: function(name) {
                table_node = document.createElement(name);
                return table_node;
            },
            create_frame: function() {
                var _div = document.createElement("div");
                _div.setAttribute("id", "contest_detail");
                var _table = this.__create_tag("table");
                _div.appendChild(_table);
                return _div
            },
            create_movie_html: function(count) {
                return "" +
                    "<h3 id='title'>動画" + count + "</h3>" +
                    "<table>" +
                    "  <tr>" +
                    "    <th>動画リンク" +
                    "      <span class='must'>必須</span></th>" +
                    "    <td colspan='3'>" +
                    "      <input type='text' " +
                    "         class='movie_link'" +
                    "         name='movie_link" + count + "'></td>" +
                    "  </tr>" +
                    "  <tr>" +
                    "    <th>開始秒" +
                    "      <span class='option'>任意</span></th>" +
                    "    <td>" +
                    "      <input type='text' " +
                    "             name='start_time" + count + "'>" +
                    "    </td>" +
                    "    <th>終了秒" +
                    "      <span class='option'>任意</span></th>" +
                    "    <td>" +
                    "      <input type='text' " +
                    "             name='end_time" + count + "'>"+
                    "    </td>" +
                    "  </tr>" +
                    "  <tr>" +
                    "    <th>滑走者 " +
                    "      <span class='must'>必須</span>" +
                    "    </th>" +
                    "    <td>" +
                    "      <input type='text' " +
                    "             name='player" + count + "'>"+
                    "    </td>" +
                    "  </tr>" +
                    "</table>"
            }
        };
        // main process
        var count = number.__count();
        number.__add(count);
        frame = links.create_frame();
        frame.innerHTML = links.create_movie_html(count);
        links.append_top("input", frame);
    }
};
