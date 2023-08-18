from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post, Comment

@csrf_exempt
def add_comment(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            content = data['content']

            # Create a new comment object and associate it with the post
            comment = Comment(post=post, content=content)
            comment.save()

            return JsonResponse({'message': 'Comment added successfully'})
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)

def get_comment_detail_as_json(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        comments = Comment.objects.filter(post=post)
        comments_json = [
            {
                'id': comment.id,
                'content': comment.content,
            }
            for comment in comments
        ]
        return JsonResponse({'comments': comments_json})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)