/* insert test judge */
insert into judge_master(
    judge_first_name,
    judge_last_name,
    judge_nickname,
    judge_capacity,
    email,
    register_time
)
values (
    "テスト",
    "ユーザー",
    "テスター",
    3,
    "judge_test@test.com",
    "2014-08-25"
);

/* insert test player */
insert into player_master(
    player_name,
    player_nickname,
    degree,
    country
)
values (
    "テストプレーヤー",
    "ぴよ",
    4,
    0
);

/* insert new score */
insert into obo_score(
    contest_no,
    skating_no,
    player_no,
    player_type,
    judge_user,
    technical_merit,
    presentation
)
values (
    1,
    2,
    1,
    2,
    1,
    49,
    39
    );

/* insert new movie */
insert into contest_movie(
    player_no,
    contest_no,
    url,
    start_time,
    end_time
)
values (
    0,
    0,
    "http://youtu.be/FHjf25eDWJA",
    29,
    314
);


