from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from item.models import item
from. models import conversation as convo
from . form import conversationMessageForm

def new_conversation(request,item_pk):
    print(item_pk)
    
    # getting the object of the item which the conversation is about
    item_about_conversation = get_object_or_404(item,pk = item_pk)

    if item_about_conversation.created_by == request.user:
        return redirect('dashboard:dashboard')
    
    # getting the object of coversation   - filter them by item will get all the 
    # conversations about this item (can have more coversaation with diff users )
    # so filter by members in coversation
    conversations = convo.objects.filter(item = item_about_conversation).filter(members__in= [request.user.id])

    if conversations:
        return redirect('conversation:detail',pk =conversations.first().id)
    if request.POST:
        form =  conversationMessageForm(request.POST)

        if form.is_valid():
            conversation_obj = convo.objects.create(item=item_about_conversation)
            conversation_obj.members.add(request.user)
            conversation_obj.members.add(item_about_conversation.created_by)
            conversation_obj.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation_obj
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('Item:details',pk = item_pk)
        
    else:
        form = conversationMessageForm()

    return render(request,'conversation/new.html',{'form':form})


def inbox(request):
    conversations = convo.objects.filter(members__in= [request.user.id])

    return render(request,'conversation/inbox.html',{'conversations':conversations})

def details(request,pk):
    conversations = convo.objects.filter(members__in= [request.user.id])
    conversation_instance = conversations.get(pk=pk)
    if request.POST:
        form =  conversationMessageForm(request.POST)
        conversation_instance = conversations.get(pk=pk)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation_instance
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation_instance.save()

            return redirect('conversation:detail',pk = pk)
        
    else:
        form = conversationMessageForm()

    return render(request,'conversation/detail.html',{'conversations':conversation_instance,'form':form})





