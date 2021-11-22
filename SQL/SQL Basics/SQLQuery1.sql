--Creating database.

CREATE DATABASE SchoolDB;


--Creating data tables.

CREATE TABLE students (
	id INT IDENTITY(1, 1) PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	birth_date DATE,
	class_id INT,
	major_id INT,
	class_teacher_id INT,
	spec_course_id INT
);

CREATE TABLE classes (
	id INT IDENTITY(10, 1) PRIMARY KEY,
	class_name VARCHAR(5) NOT NULL UNIQUE
);

CREATE TABLE majors (
	id INT IDENTITY(20, 1) PRIMARY KEY,
	major_name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE class_teachers (
	teacher_id INT PRIMARY KEY,
	class_id INT
);

CREATE TABLE teachers (
	id INT IDENTITY(30, 1) PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	birth_date DATE,
	salary INT,
	major_id INT,
	spec_course_id INT
);

CREATE TABLE spec_courses (
	id INT IDENTITY(50, 1) PRIMARY KEY,
	spec_course_name VARCHAR(20) NOT NULL UNIQUE
);


--Modifying data tables.

ALTER TABLE class_teachers 
ADD FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
	FOREIGN KEY(class_id) REFERENCES classes(id) ON DELETE SET NULL;

ALTER TABLE teachers
ADD FOREIGN KEY(spec_course_id) REFERENCES spec_courses(id) ON DELETE SET NULL,
	FOREIGN KEY(major_id) REFERENCES majors(id) ON DELETE SET NULL;

ALTER TABLE students 
ADD FOREIGN KEY(class_id) REFERENCES classes(id) ON DELETE SET NULL,
	FOREIGN KEY(major_id) REFERENCES majors(id) ON DELETE SET NULL,
	FOREIGN KEY(class_teacher_id) REFERENCES class_teachers(teacher_id) ON DELETE SET NULL,
	FOREIGN KEY(spec_course_id) REFERENCES spec_courses(id) ON DELETE SET NULL;


--Inserting data in data tables.

INSERT INTO classes VALUES('8-D');
INSERT INTO classes VALUES('10-A');
INSERT INTO classes VALUES('6-C');
INSERT INTO classes VALUES('1-B');

INSERT INTO spec_courses VALUES('Math');
INSERT INTO spec_courses VALUES('English');
INSERT INTO spec_courses VALUES('Art');

INSERT INTO majors VALUES('Biology');
INSERT INTO majors VALUES('Sociology');
INSERT INTO majors VALUES('Geometry');
INSERT INTO majors VALUES('Geography');

INSERT INTO teachers VALUES('Miranda', 'Dunlap', '1988-06-07', 2600, 20, NULL);
INSERT INTO teachers VALUES('Syed', 'Singh', '1989-09-06', 2400, 21, 51);
INSERT INTO teachers VALUES('Samina', 'Branch', '1991-08-01', 2650, 23, 52);
INSERT INTO teachers VALUES('Aled', 'Pena', '1985-01-02', 2750, 22, 50);

INSERT INTO class_teachers VALUES(30, 10);
INSERT INTO class_teachers VALUES(31, 11);
INSERT INTO class_teachers VALUES(33, 12);
INSERT INTO class_teachers VALUES(32, 13);

INSERT INTO students VALUES('Lucie', 'Dalton', '2004-12-12', 10, 20, 30, 50);
INSERT INTO students VALUES('Aydin', 'Hays', '2002-03-04', 11, 20, 31, 50);
INSERT INTO students VALUES('Emma', NULL, '2006-06-05', 12, 22, 33, 51);
INSERT INTO students VALUES('Emma', NULL, '2006-06-05', 12, 23, 33, 51);
INSERT INTO students VALUES('Eliott', 'Richard', '2011-09-08', 13, 22, 32, 52);


--Deleting data tables.

DROP TABLE students;
DROP TABLE class_teachers;
DROP TABLE teachers;
DROP TABLE majors;
DROP TABLE classes;
DROP TABLE spec_courses;
