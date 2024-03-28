-- query soal a
SELECT AVG(mentor_satisfaction_score) AS avarage_mentor_satisfaction
FROM `data-playground-418513.survey_dataset.survey`;

-- query soal b
SELECT AVG(cs_satisfaction_score) AS avarage_cs_satisfaction
FROM `data-playground-418513.survey_dataset.survey`;

-- query soal c
SELECT AVG(mentor_satisfaction_score) AS avarage_mentor_satisfaction_course_a
FROM `data-playground-418513.survey_dataset.survey`
WHERE course_name = 'Course A';

-- query soal d
SELECT MIN(learning_satisfaction_score) AS min_learning_satisfaction_course_c
FROM `data-playground-418513.survey_dataset.survey`
WHERE course_name = 'Course C';

-- query soal e
SELECT MAX(cs_satisfaction_score) AS max_cs_satisfaction_course_b
FROM `data-playground-418513.survey_dataset.survey`
WHERE course_name = 'Course B';

-- query soal f
SELECT course_name
FROM `data-playground-418513.survey_dataset.survey`
GROUP BY course_name
ORDER BY AVG(mentor_satisfaction_score) DESC
LIMIT 1;

-- query soal g
SELECT course_name
FROM `data-playground-418513.survey_dataset.survey`
GROUP BY course_name
ORDER BY AVG(learning_satisfaction_score) DESC
LIMIT 1;