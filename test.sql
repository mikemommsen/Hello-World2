begin;
create table tester (
	a text,
	b text,
	c int)
;
insert into tester values('a','b',3);
insert into tester values('b','a',4);
insert into tester values('b','a',5);
insert into tester values('b','a',7);
commit;
