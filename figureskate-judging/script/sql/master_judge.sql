insert into judge_master(
    judge_first_name,
    judge_last_name,
    judge_nickname,
    judge_capacity,
    email,
    register_time
    )
    values(
        'judge_master',
        'piyo',
        'master',
        0,
        'master@pyohei.com',
        DATE(NOW())
    );

insert into judge_password(
    judge_no,
    password
    )
    values(
        1,
        '409e41eb60e44da6dffb66a710a0a7df77b65c9a94e076d3d525660e'
    );
