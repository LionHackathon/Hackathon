from django.http import JsonResponse
from django.views import View
from .models import Post
import json
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_as_json(request):
    if request.method == "GET":
        posts = Post.objects.all()
        posts_json = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'createdDate': post.createdDate.strftime('%Y-%m-%d %H:%M:%S')
            }
            for post in posts
        ]
        return JsonResponse({'posts': posts_json})

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            title = data['title']
            content = data['content']

            # Create a new post object
            post = Post(title=title, content=content)
            post.save()

            return JsonResponse({'message': 'Post created successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_post_detail_as_json(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'createdDate': post.createdDate.strftime('%Y-%m-%d %H:%M:%S'),  # 날짜 포맷 지정
    }
    return JsonResponse(post_data)