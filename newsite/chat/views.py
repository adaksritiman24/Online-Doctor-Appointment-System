from django.shortcuts import redirect, render

# Create your views here.
def main_view(request):
    context = {'room_name':'rbxxy524'}
    return render(request, 'chat/main.html', context=context)

def index(request):
    if request.method == "GET":
        return render(request, 'chat/index.html')
    else:
        user = request.POST['user']
        request.session['user'] = user
        return render(request, 'chat/index.html')    