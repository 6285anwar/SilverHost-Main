from django.http import HttpResponseForbidden

class RestrictMobileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

        if 'mobi' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
            return HttpResponseForbidden('Access denied from mobile devices.')

        response = self.get_response(request)
        return response