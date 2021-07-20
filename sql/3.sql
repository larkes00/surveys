SELECT question_id, COUNT(question_id)
FROM surveys_answer
GROUP BY question_id
