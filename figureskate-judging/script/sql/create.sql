/* Contest list */
create table contest_master (
    contest_no int(10) not null auto_increment,
    contest_name varchar(255),
    contest_type int(8) not null default 0,
    judge_type tinyint(4) not null default 0,
    contest_date date,
    invalid tinyint(2) not null default 0,
    update_user tinyint(4) default 0,
    update_time timestamp not null,
    primary key(
        contest_no),
    index (
        contest_no,
        contest_type,
        judge_type
        )
    );

/* Judge list */
create table judge_master (
    judge_no int(10) not null auto_increment,
    judge_first_name varchar(255),
    judge_last_name varchar(255),
    judge_nickname varchar(255) not null default 'unknownuser',
    judge_capacity varchar(10) not null default 'a',
    email varchar(255) not null,
    judging_time int(6) default 0,
    register_time datetime,
    invalid tinyint(2) not null default 0,
    update_user tinyint(4) default 0,
    update_time timestamp not null,
    primary key(
        judge_no),
    index (
        judge_no,
        judge_nickname,
        judge_capacity
        )
    );

/* player master */
create table player_master (
    player_no int(10) not null auto_increment,
    player_name varchar(255) not null,
    player_nickname varchar(255),
    degree tinyint(2) not null default 0,
    country int(255) default 0,
    invalid tinyint(2) not null default 0,
    update_user tinyint(4) default 0,
    update_time timestamp not null,
    primary key(
        player_no),
    index(
        player_no,
        player_name,
        player_nickname,
        degree
        )
    );

/* session manager */
create table session (
    session_no int(12) not null auto_increment,
    session_id varchar(255) not null,
    limit_datetime datetime not null,
    judge_no int(10) not null,
    update_time timestamp,
    update_user int(10) default 0,
    primary key(
        session_no),
    unique(
        session_id),
    index(
        session_no,
        judge_no)
    );

/* password manager */
create table Judge_password (
    judge_no int(12) not null,
    password varchar(100) not null,
    update_time timestamp,
    update_user int(10) default 0,
    primary key(
        judge_no),
    unique(
        password),
    index(
        judge_no)
    );

/* contest_movie */
create table contest_movie (
    movie_no int(12) not null auto_increment,
    player_no int(10) not null,
    contest_no int(12) not null,
    url varchar(255) not null,
    start_time int(10) default null,
    end_time int(10) default null,
    update_time timestamp,
    update_user int(10) default 0,
    primary key(
        movie_no),
    index(
        movie_no,
        player_no,
        contest_no
        )
    );


