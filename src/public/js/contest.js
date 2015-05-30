var select_contest = function (no) {
    var contest_no = document.getElementsByName("contest_no");
    //alert(no);
    contest_no[0].value = no;
    document.main.submit();
}
