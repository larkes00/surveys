-- 3) Написать запросы:
-- - Количество опросов, созданных каждым пользователем
-- - Количество вопросов, созданных каждым пользователем
-- - Количество ответов, созданных каждым пользователем
SELECT surveys_user.id, surveys_user.name, COUNT(author_id) AS surveys_count
FROM surveys_survey
RIGHT JOIN surveys_user
ON surveys_user.id = surveys_survey.author_id
GROUP BY surveys_user.id
ORDER BY surveys_count DESC;

SELECT surveys_user.id, surveys_user.name, COUNT(author_id) AS surveys_count
FROM surveys_survey
JOIN surveys_user
ON surveys_user.id = surveys_survey.author_id
GROUP BY surveys_user.id
ORDER BY surveys_count DESC;
 -------------------------------------------------
SELECT author_id, COUNT(author_id)
FROM surveys_surveyquestion
JOIN surveys_survey 
ON surveys_survey.id = surveys_surveyquestion.survey_id
GROUP BY author_id;
--------------------------------------------
SELECT author_id, COUNT(author_id)
FROM surveys_answer
JOIN surveys_question
ON surveys_answer.question_id = surveys_question.id
JOIN surveys_surveyquestion
ON surveys_surveyquestion.question_id = surveys_question.id
JOIN surveys_survey
ON surveys_surveyquestion.survey_id = surveys_survey.id
GROUP BY author_id;
-----------------------------

SELECT complete_survey.id ,survey.name,
        complete_survey_question.question_id,
        bool_or(complete_survey_question.answer_id is null ) and
        bool_or(question_answer.is_correct is TRUE )
    FROM surveys_completesurvey as complete_survey
    JOIN surveys_completesurveyquestion as complete_survey_question ON complete_survey_question.complete_survey_id = complete_survey.id
    JOIN surveys_survey as survey ON survey.id = complete_survey.survey_id
    FUll OUTER JOIN surveys_questionanswer as question_answer ON question_answer.answer_id = complete_survey_question.answer_id and
        question_answer.question_id = complete_survey_question.question_id
    WHERE survey.type = 'Test'
    GROUP BY complete_survey.id, survey.name, complete_survey_question.question_id;