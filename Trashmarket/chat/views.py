from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from items.models import Items

from .models import Chat
from .forms import ChatMessageForm


@login_required
def new_chat(request, item_pk):
    item = get_object_or_404(Items, pk=item_pk)

    if item.created_by == request.user:
        return redirect('mainpage:index')

    chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])

    if chats:
        return redirect('chat:detail', pk=chats.first().id)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            return redirect('items:detail', pk=item_pk)
    else:
        form = ChatMessageForm()

    return render(request, 'new.html', {'form': form})


@login_required
def inbox(request):
    chats = Chat.objects.filter(members__in=[request.user.id])

    return render(request, 'inbox.html', {'chat': chats})


@login_required
def detail(request, pk):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect('chat:detail', pk=pk)
    else:
        form = ChatMessageForm()

    return render(request, 'detail.html', {'chat': chat, 'form': form})
