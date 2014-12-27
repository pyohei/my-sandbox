/* obo score table */
create table obo_score (
    score_no int(10) not null auto_increment,
    contest_no int(8) not null default 0,
    skating_no int(8) not null default 0,
    player_no int(8) not null default 0,
    player_type int(8) not null default 0,
    judge_user int(8) not null default 0,
    technical_merit tinyint(3) not null default 0,
    presentation tinyint(3) not null default 0,
    update_user tinyint(4) default 0,
    update_time timestamp not null,
    primary key(score_no),
    index (
        score_no,
        contest_no,
        skating_no,
        player_no)
);

