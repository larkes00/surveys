INSERT INTO surveys_user(id, name) VALUES 
(1, 'Tom'), (2, 'Ban'), (3, 'Bob'), (4, 'Alex'), (5, 'Steve'), (6, 'Alice'), (7, 'Jhon'), (8, 'Sten');
INSERT INTO surveys_question(id, content) VALUES 
(1, 'Did you graduate from high school?'), (2, 'How do you rate medicine in your country from 1 to 10?'), 
(3, 'Should people protect nature?'), (4, 'What''s your gender?'), (5, 'Are you from Ukraine?'), (6, 'Do you have a university degree'), 
(7,'Did you get a job after graduating from university?'), (8, 'Need a change in healthcare?'), 
(9, 'In your opinion, it is necessary to stop deforestation?'), (10, 'Who do you think is faster than an ostrich or a cheetah?'), 
(11, 'Are you proud of who you have become?'), (12, 'Are you married?');
INSERT INTO surveys_answer(id, content, question_id) VALUES 
(1,'Yes', 1), (2, 'No', 1), (3,'1', 2), (4, '2', 2), (5,'3',2 ), (6, '4', 2), (7,'5', 2), (8, '6', 2), (9,'7', 2), 
(10, '8', 2), (11, '9', 2), (12, '10', 2), (13,'Yes', 3), (14, 'No', 3), (15,'Male', 4), (16, 'Female', 4), (17,'Yes', 5), 
(18, 'No', 5), (19,'Yes', 6), (20, 'No', 6), (21,'Yes', 7), (22, 'No', 7), (23,'Yes', 8), (24, 'No', 8), (25,'Yes', 9), 
(26, 'No', 9), (27,'Ostrich', 10), (28, 'Cheetah', 10), (29, 'Yes', 11), (30, 'No', 11), (31, 'Yes', 12), (32, 'No', 12);
INSERT INTO surveys_surveyarea(id, name) VALUES 
(1, 'Personal'), (2, 'Education'), (3, 'Medicin'), (4, 'Nature');
INSERT INTO surveys_survey(id, name, author_id, area_id) VALUES 
(1,'About myself',  6,1), (2,'The level of education', 6, 2), (3,'Medicine reviews',2, 3), (4,'Attitude to nature',1, 4);
INSERT INTO surveys_surveyquestion(id, survey_id, question_id) VALUES 
(1, 1, 4), (2, 1, 5), (3, 2, 1), (4,2, 6), (5, 1, 7), (6, 3, 2), (7, 3, 8), (8, 4, 10), (9,4, 3), (10,4, 9), (11, 1, 11), (12, 1, 12);
UPDATE surveys_survey SET type = 'Formal';
INSERT INTO surveys_surveyarea(id, name) VALUES
(5, 'Math');
INSERT INTO surveys_question(id, content) VALUES 
(13, '5 + 5 = ?'), (14, '2 / 2 = ?'), (15, 'x + 1 = 0. x = ?'), (16, '2 + 2 * 2 = ?');
INSERT INTO surveys_answer(id, content, question_id) VALUES 
(33, '10', 13), (34, '11', 13), (35, '1', 14), (36, '-1', 14), (37, '1', 15), (38, '-1', 15), (39, '6', 16), (40, '8', 16);
UPDATE surveys_question SET correct_answer_id = 33 WHERE id = 13;
UPDATE surveys_question SET correct_answer_id = 35 WHERE id = 14;
UPDATE surveys_question SET correct_answer_id = 38 WHERE id = 15;
UPDATE surveys_question SET correct_answer_id = 39 WHERE id = 16;
INSERT INTO surveys_survey(id, name, author_id, area_id, type) VALUES 
(5,'Math usual test', 6, 5, 'Test');
INSERT INTO surveys_surveyquestion(id, survey_id, question_id) VALUES 
(13, 5, 13), (14, 5, 14), (15, 5, 15), (16, 5, 16);
INSERT INTO surveys_completesurvey (survey_id, user_id, answer_id, question_id, completed_at) VALUES
(5, 8, 34, 13, '2020-11-4'), (5, 8, 35, 14, '2020-11-4'), (5, 8, 38, 15, '2020-11-4'), (5, 8, 40, 16, '2020-11-4'),
(2, 3, 1, 1, '2020-12-5'), (2, 3, 20, 1, '2020-12-5'), (4, 4, 13, 3, '2020-12-5'), (4, 4, 25, 9, '2020-12-5'), (4, 4, 27, 10, '2020-12-5'), 
(3, 5, 7, 2, '2020-8-22'), (3, 5, 23, 8, '2020-8-22'), (2, 7, 15, 4, '2020-10-19'), (2, 7, 19, 5, '2020-10-19'), (2, 7, 29, 11, '2020-10-19'), (
2, 7, 32, 12, '2020-10-19');