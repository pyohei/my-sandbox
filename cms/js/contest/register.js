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
            __add_title: function(count, _id) {
                var title = "動画番号" + count;
                var h = this.__create_h_tag(title, "3");
                document.getElementById(_id).insertBefore(h,document.getElementById(_id).firstChild);
            },
            __add_link: function(count, _id) {
                var p = this.__create_p_tag("動画リンク");
                var input = this.__create_input_tag("movie_link");
                p.appendChild(input);
                document.getElementById(_id).insertBefore(p,document.getElementById(_id).firstChild);
            },
            __add_start_time: function(count, _id) {
                var p = this.__create_p_tag("開始秒");
                var input = this.__create_input_tag("start_time");
                p.appendChild(input);
                document.getElementById(_id).insertBefore(p,document.getElementById(_id).firstChild);
            },
            __add_end_time: function(count, _id) {
                var p = this.__create_p_tag("終了秒");
                var input = this.__create_input_tag("end_time");
                p.appendChild(input);
                document.getElementById(_id).insertBefore(p,document.getElementById(_id).firstChild);
            },
            __add_player: function(count, _id) {
                var p = this.__create_p_tag("滑走者");
                var input = this.__create_input_tag("player");
                p.appendChild(input);
                document.getElementById(_id).insertBefore(p,document.getElementById(_id).firstChild);
            },
            __create_p_tag: function(text_value) {
                var p_node = document.createElement("p");
                p_node.innerText = text_value;
                return p_node;
            },
            __create_input_tag: function(name_value) {
                var input_node = document.createElement("input");
                input_node.setAttribute("type", "text");
                input_node.setAttribute("name", name_value+count);
                return input_node;
            },
            __create_h_tag: function(text, number) {
                var h_tag = "h";
                if (number === undefined) {
                    h_tag = "h1";
                } else {
                    h_tag += number;
                }
                alert(h_tag);
                var h_node = document.createElement(h_tag);
                h_node.innerText = text;
                return h_node;
            },
        };

        // main process
        var count = number.__count();
        number.__add(count);
        links.__add_title(count, "input");
        links.__add_link(count, "input");
        links.__add_start_time(count, "input");
        links.__add_end_time(count, "input");
        links.__add_player(count, "input");
    }
};
