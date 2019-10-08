from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

@cache_control(private=True)
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>It works!</h1>
            <p>Greetings from Zeit Now 2.0 at { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
