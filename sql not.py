Table 作成(Create)
            create table TableName
            (no varchar(7),passwd varchar(15),
            name varchar(20),family int);//column create
    
Tableの削除(Drop)
            Drop table TableName;
            
Databaseの削除
            Drop database DatabaseName

Tableに値を入れる(Insert Into)挿入
            Insert into table name(table column name)
            -values(..,..,..,..);
            
            略
             insert into tablename
             -values(..,..,..,..);
    
Tableの操作(Alter Table)
            ALTER TABLE ADD (Columnの追加)
            ALTER TABLE tablename ADD  columnname varchar(50) after name;
           
            ALTER TABLE DROP (Columnの削除)
            ALTER TABLE tablename Drop  columnname;
            
            CHANGE (column名を変更する)
            ALTER TABLE tablename Change OldColumnName NewColumnName DataItem;  
            
            CONIFIRM (Columnを確認する)
            show fields from TableName;
            
            UPDATE SET (Valeを変更するとき)
            Update tablename set columnname = 'newvalue' wher no = 'Value';
           
            SELECT FROM (Tableを検査する)
            1.select * from TableName;
            2.select ColumnName from TableName;
            
Delete value select row(Delete)
            Delete from Tablename where ColumnName = 'Value';

            Delete from Tablename
            -where ColumnName = 'Value';
            Up
抽出条件を指定する（レコードの絞り込む)
            
            Where句(レコードを条件で絞り込む込む)
            Select * from Tablename
            where ColumnName = 'Value';
            
            Between演算子はフィールドの値が指定された範囲に含まれるかどうかを判定する
            Select * from Tablename
            Where ColumnName Between 'Value' AND 'Value';
            
            IN(Where In)演算子は例挙された候補値のどれかに合致するものを取り出す
            ORと似ていいる
            Select * from Tablename
            Where ColumnName IN(Value,Value);

曖昧な検索(Like %);
            Select * from Tablename
            where ColumnName Like 'Characer%'
            
レコードの並べ替え(Order By)It's called sort.
            ASC- Start Small to Big
            DESC- Start Big to Small
            Select * from Tablename
            Order by ColumnName ASC;
            
レコードの集計(Grouped By)
            select score,count(*) from Tablename
            group by ColumnName;
            
関数
            ROUNDAVG
            select round(avg(ColumnName) As NewColumnName from TableName)
            round avg is describe Integer.Not double.
            
            AVG
            select AVG(ColumnName)
            from TableName;
            
            COUNT
            select count(ColumnName)
            from TableName
            where ColumnName = 'Value';
            
            SUM
            select SUM(ColumnName)
            from TableName;
            
            Max
            select Max(ColumnName)
            from TableName
            
            MIN
            select MIN(ColumnName)
            from TableName
            
主キー(Primary Key)
            NULLは入力できない
            二つになれないColumnは主キーになる
            Alter Table TableName ADD Primary Key (ColumnName);
     
            確認する
            show fields from TableName;

データ型
            文字列
            Char(固定長文)
            varchar（可変長文））
            Text（長いテキスト　2¹⁶-1バイト)
            
            数値
            Int(214....to-214......)(unsingned 0 to 429......)
            Double(-1.7 to 1.7)
            
            日付
            DATETIME(日付／時刻)
            DATE(日付)
            TIME(時刻)
            
索引(Index)
            文字順に処理されたインデックスからレコードの位置を知る
            巻末の索引でキーワードを探し、直接、目的を探す
            まずはIndexを作成する
            create index idx_TableName On TableName (ColumnNane);
            explain select ColumnName from TableName
            -where column = 'Valur'
            
            Drop index idx_TableName On TableName

トランザクション(Transaction)
            開始-処理-終了
            Begin-(Commit)Select * from TableName where ColumnName = 'Value'-RollBackRollBack
 
結合(JOIN ON)
            INNER JOIN/JOIN (Left Outer Join)(Right Oute Join)
            Select NewTableName.ColumnName
            //Select s.st,f.psswd 
             from TableName as NewTableName
            //from student as s
            Inner Join TableName as NewTableName On 
            //Inner Join family as f On
            NewTableName.ColumnName = NewTableName.ColumnName(SameColumnName)
            //s.st = f.st
            where NewTableName.ColumnName = 'Value'
            //where s.score = '78';
            
            

   