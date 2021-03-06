from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8)


class SignupSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8)


# class CompleteSurveySerializer(serializers.Serializer):
#     user_id = serializers.IntegerField(required=True)
#     survey_id = serializers.IntegerField(required=True)
#     question_id = serializers.IntegerField(required=True)
#     answer_id = serializers.IntegerField(required=True)


class SurveySerializer(serializers.Serializer):
    author_id = serializers.IntegerField(required=True)
    area_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    type = serializers.CharField(required=True)


class QuestionSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    correct_answer_id = serializers.IntegerField(required=True)


class SurveyAreaSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class SurveyAreaDeleteSerializer(serializers.Serializer):
    survey_area_id = serializers.IntegerField(required=True)


class AnswerSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    question_id = serializers.IntegerField(required=True)


class CompleteSurveyQuestionsSerializer(serializers.Serializer):
    question_id = serializers.IntegerField(required=True)
    answer_id = serializers.IntegerField(required=True)


class CompleteSurveySerializer(serializers.Serializer):
    questions = CompleteSurveyQuestionsSerializer(required=True, many=True)
    survey_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)


class QuestionDeleteSerializer(serializers.Serializer):
    question_id = serializers.IntegerField(required=True)


class SurveyDeleteSerializer(serializers.Serializer):
    survey_id = serializers.IntegerField(required=True)


class AnswerDeleteSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField(required=True)
    survey_id = serializers.IntegerField(required=True)
