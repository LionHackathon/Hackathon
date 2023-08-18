from django.http import JsonResponse
from django.views import View
from .models import Question
import json
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from answer.models import Answer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def questions_as_json(request):
    if request.method == "GET":
        questions = Question.objects.all()
        questions_json = [
            {
                'id': question.id,
                'title': question.title,
                'content': question.content,
                'createdDate': question.createdDate.strftime('%Y-%m-%d %H:%M:%S')
            }
            for question in questions
        ]
        return JsonResponse({'questions': questions_json})

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            title = data['title']
            content = data['content']

            # Create a new question object
            question = Question(title=title, content=content)
            question.save()

            return JsonResponse({'message': 'Question created successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_question_detail_as_json(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_data = {
        'id': question.id,
        'title': question.title,
        'content': question.content,
        'createdDate': question.createdDate.strftime('%Y-%m-%d %H:%M:%S'),  # 날짜 포맷 지정
    }
    return JsonResponse(question_data)

def home(request):
    return render(request, 'question.html')

def question_write(request):
    return render(request, 'write.html')