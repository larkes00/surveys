SELECT survey_id, COUNT(survey_id)
FROM surveys_surveyquestion
GROUP BY survey_id
ORDER BY survey_id;


