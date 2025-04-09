from django.http import HttpResponse
import pprint

def debug_request(request):
    request_data = {
        "user": str(request.user),
        "user.groups.all()": list(request.user.groups.all()),
        "request.user.role": request.user.role,
        # "user": str(request.user),
        # "attributes": dir(request),
        # "meta": dict(request.META),
        # "get": request.GET.dict(),
        # "post": request.POST.dict(),
        # "cookies": request.COOKIES,
    }
    pretty_data = pprint.pformat(request_data, indent=4)
    return HttpResponse(f"<pre>{pretty_data}</pre>")
