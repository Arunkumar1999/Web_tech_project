create table product(
	pname varchar(30),
	product_code varchar(10),
	primary key (product_code)
	);
create table raw_material
	(	
		product_code varchar(10),
		preform bigINT,
		Lebel bigINT,
		cap bigINT,
		carton bigINT,
		tape int ,
		raw_date date not null,
		status varchar(15) not null,
			);
	create table twyL_raw
	(	
		product_code varchar(10),
		cans bigINT,
		dispenser bigINT,
		twyL_cap bigINT,
		twyL_Lebel bigINT,
		slews bigint ,
		coldcans bigINT,
		r_date date not null,
		status varchar(15) not null,
		);

CREATE TABLE DEPARTMENT
      (
       DEPTNAME  VARCHAR(30)       NOT NULL,
       PRIMARY KEY (DEPTNAME));
CREATE TABLE EMPLOYEE
      (EMPNO       CHAR(6)         NOT NULL,
       FIRSTNME    VARCHAR(15)     NOT NULL,
       LASTNAME    VARCHAR(15)     NOT NULL,
       WORKDEPT    CHAR(10)                 ,
       PHONENO     bigint                 ,
       HIREDATE    DATE                    ,
       JOB         CHAR(8)                 ,
       SEX         CHAR(5)                 ,
       BIRTHDATE   DATE                    ,
       SALARY      DECIMAL(9,2)            ,
       PRIMARY KEY (EMPNO),
       CONSTRAINT Red FOREIGN KEY (WORKDEPT) REFERENCES DEPARTMENT(DEPTNAME) ON DELETE SET NULL
       );
CREATE TABLE SALARY_details
(
	EMPNO CHAR(6) ,
	issued bigint NOT NULL,
	balence bigint not null,
	iss_date date not null,
	CONSTRAINT eno FOREIGN KEY (EMPNO) REFERENCES EMPLOYEE(EMPNO) ON DELETE SET NULL


);

insert into product values('1L','1L');
insert into product values('1L','2L');
insert into product values('1/2L','1/2L');
insert into product values('20L','20L');
insert into product values('Cold','cold');

insert into raw_material values('2L',50,40,47,68,10,2019-04-24);
insert into raw_material values('2L',70,74,45,78,40,2019-04-25);
insert into raw_material values('3L',60,12,45,40,10,2019-04-30);
insert into raw_material values('1L',44,45,40,10,05,2019-05-02);
insert into raw_material values('1L',50,45,70,10,07,2019-05-05);

insert into twyl_raw values('20L',500,100,1000,500,1000,null,2019-06-10,'added');
insert into twyl_raw values('20L',500,100,1000,500,1000,null,2019-06-10,'added');
insert into twyl_raw values('20L',500,100,1000,500,1000,null,2019-06-10,'added');
	insert into twyl_raw values('20L',500,100,1000,500,1000,null,2019-06-10,'alter');