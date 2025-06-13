mysqlの基本データ型
MySQL の文字列型（char,varchar,...)
MySQL の数値型  （int,smallint,...)(double,float,....)
MySQL の日付と時間型 (date - 'y-m-d')(datetime - 'y-m-d h:m:s')(time - 'h:m:s:')(year - '----')

文法
create table
CREATE TABLE students (
    student_id      INT             NOT NULL AUTO_INCREMENT,
    student_number  VARCHAR(10)     NOT NULL,
    first_name      VARCHAR(50)     NOT NULL,
    last_name       VARCHAR(50)     NOT NULL,
    middle_name     VARCHAR(50)     NULL,
	birthday  	    DATE            NOT NULL,
    gender          ENUM ('M','F')  NOT NULL,
    paid_flag       BOOL            NOT NULL DEFAULT FALSE,
    PRIMARY KEY (student_id),
    UNIQUE KEY (student_number),
    CHECK (birthday >= '2000-01-01')
);

CREATE TABLE courses (
	course_id 	INT         NOT NULL AUTO_INCREMENT,
    course_name VARCHAR(20)	NOT NULL,
    PRIMARY KEY (course_id)
);

CREATE TABLE student_courses (
    student_id	INT NOT NULL,
    course_id	INT NOT NULL,
	PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id),
	FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

このスクリプトを実行すると次のようになりテーブルが三つ生成されました。

/////////////////////////
PRIMARY KEY（主キー）
その列の値は重複できない（ユニーク）
NULL を入れることはできない
テーブルごとに 1つだけ 定義できる

////////////////////////
UNIQUE KEY（ユニークキー）
その列の値は重複できない
NULL はOK（ただし DBMS によっては NULL 同士も「重複しない」と見なされる）
複数の列に対して設定可能（テーブルに複数個 OK）

////////////////////////
CHECK（チェック制約）
その列に入る値に条件をつける
条件に合わない値はエラーになります
MySQL 8.0 以降で本格的にサポート（それ以前は無視されることがありました）
