from django.shortcuts import redirect, render

# Create your views here.
def main_view(request, room_name):
    context = {'room_name': room_name,'user': request.user.id}
    return render(request, 'chat/main.html', context=context)