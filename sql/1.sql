SELECT surveys_survey.id, surveys_surveyarea.name ,surveys_question.content, surveys_answer.content
FROM surveys_question
JOIN surveys_answer 
ON surveys_question.id = surveys_answer.question_id
JOIN surveys_surveyquestion
ON surveys_surveyquestion.question_id = surveys_question.id 
JOIN surveys_survey
ON surveys_survey.id = surveys_surveyquestion.survey_id
JOIN surveys_surveyarea 
ON surveys_surveyarea.id= surveys_survey.area_id;



select surveys_surveyarea.name, COUNT(surveys_survey.id)
from surveys_survey
JOIN surveys_surveyarea ON surveys_survey.area_id = surveys_surveyarea.id
GROUP BY surveys_surveyarea.name;


select surveys_surveyarea.name, surveys_survey.name, COUNT(question_id)
from surveys_surveyquestion
JOIN surveys_survey ON surveys_surveyquestion.survey_id = surveys_survey.id
JOIN surveys_surveyarea ON surveys_survey.area_id = surveys_surveyarea.id
GROUP BY surveys_surveyarea.name, surveys_survey.name
ORDER BY surveys_surveyarea.name, surveys_survey.name


select surveys_surveyarea.name, surveys_survey.name, surveys_question.content
from surveys_surveyquestion
JOIN surveys_survey ON surveys_surveyquestion.survey_id = surveys_survey.id
JOIN surveys_surveyarea ON surveys_survey.area_id = surveys_surveyarea.id
JOIN surveys_question ON surveys_surveyquestion.question_id = surveys_question.id
ORDER BY surveys_surveyarea.name, surveys_survey.name

select surveys_surveyarea.name, surveys_survey.name, surveys_question.content, surveys_answer.content
from surveys_surveyquestion
JOIN surveys_survey ON surveys_surveyquestion.survey_id = surveys_survey.id
JOIN surveys_surveyarea ON surveys_survey.area_id = surveys_surveyarea.id
JOIN surveys_question ON surveys_surveyquestion.question_id = surveys_question.id
LEFT JOIN surveys_answer ON surveys_question.correct_answer_id = surveys_answer.id
ORDER BY surveys_surveyarea.name, surveys_survey.name


select auth_user.id, username
from auth_user
WHERE auth_user.id IN (
    SELECT author_id
    FROM surveys_survey
)

select distinct auth_user.id, username
from auth_user
RIGHT JOIN surveys_survey ON surveys_survey.author_id = auth_user.id
ORDER BY username

select username, MIN(DATE(surveys_completesurvey.completed_at) - DATE(auth_user.date_joined)) as date_completed
from auth_user
join surveys_completesurvey ON auth_user.id = surveys_completesurvey.user_id
GROUP BY username
ORDER BY date_completed DESC

-- 1

INSERT INTO surveys_questionanswer (answer_id, question_id) select id, question_id from surveys_answer
UPDATE surveys_questionanswer SET is_correct = 1 WHERE surveys_question.correct_answer_id = surveys_questionanswer.answer_id FROM surveys_question

-- 3

SELECT survey.id as survey_id, COUNT(question_answer.answer_id)
FROM surveys_survey as survey
JOIN surveys_surveyquestion as survey_question ON survey_question.survey_id = survey.id
JOIN surveys_questionanswer as question_answer ON question_answer.question_id = survey_question.question_id
WHERE survey.type = 'Test' and question_answer.is_correct = TRUE
GROUP BY survey.id;