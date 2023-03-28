from werkzeug.wrappers import Request, Response
@Request.application
def application(request):
    list = ["pedro", 'elias']
    return Response("Ola servidor web")
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)