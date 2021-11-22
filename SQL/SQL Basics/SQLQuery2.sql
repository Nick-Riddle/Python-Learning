SELECT DISTINCT students.first_name, students.last_name, classes.class_name FROM students
JOIN classes
ON classes.id = students.class_id;


SELECT teachers.first_name, majors.major_name, spec_courses.spec_course_name FROM teachers
LEFT JOIN majors
ON teachers.major_id = majors.id
LEFT JOIN spec_courses
ON teachers.spec_course_id = spec_courses.id
ORDER BY teachers.first_name;


SELECT DISTINCT TOP 2 first_name, last_name, birth_date FROM students
WHERE birth_date >= '2006-01-01' AND birth_date <= '2012-01-01'; -- OR WHERE birth_date BETWEEN '2006-01-01' AND '2012-01-01';


INSERT INTO teachers VALUES('Lina', 'Lusm', '1988-06-07', 1900, NULL, 51);


SELECT COUNT(teachers.id) AS number_of_teachers, spec_courses.spec_course_name FROM teachers
JOIN spec_courses
ON spec_courses.id = teachers.spec_course_id
GROUP BY spec_courses.spec_course_name
HAVING COUNT(teachers.id) > 1;


SELECT students.first_name, majors.major_name FROM majors
JOIN students
ON students.major_id = majors.id
WHERE majors.major_name LIKE 'Geo%' or majors.major_name LIKE '%logy'

UNION 

SELECT teachers.first_name, majors.major_name FROM majors
JOIN teachers
ON teachers.major_id = majors.id
WHERE majors.major_name LIKE 'Geo%' or majors.major_name LIKE '%logy';


INSERT INTO classes VALUES('8-B');
INSERT INTO teachers VALUES('Luna', 'Genl', '1989-03-01', NULL, NULL, NULL);
INSERT INTO class_teachers VALUES(35, 14);


SELECT teachers.first_name, teachers.last_name, classes.class_name FROM class_teachers
JOIN (SELECT classes.class_name, classes.id FROM classes
WHERE classes.class_name LIKE '8%') AS classes
ON classes.id = class_teachers.class_id
JOIN teachers
ON teachers.id = class_teachers.teacher_id;
