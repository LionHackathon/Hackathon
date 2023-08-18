from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Question, Answer

@csrf_exempt
def add_answer(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            content = data['content']

            # Create a new answer object and associate it with the question
            answer = Answer(question=question, content=content)
            answer.save()

            return JsonResponse({'message': 'Answer added successfully'})
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)

def get_answer_detail_as_json(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answers = Answer.objects.filter(question=question)
        answers_json = [
            {
                'id': answer.id,
                'content': answer.content,
            }
            for answer in answers
        ]
        return JsonResponse({'answers': answers_json})
    except Question.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)
