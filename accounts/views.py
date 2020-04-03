from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.form import UserLoginForm, UserRegistrationForm, ProfileForm, MessageForm, ReplyForm
from .models import Profile, Message
from checkout.models import Order


# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, "index.html")


@login_required
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "I have been – and always shall be – your friend. Live long and prosper!")
    return redirect(reverse('index'))


def login(request):
    """ Return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                name = request.user.username
                messages.success(request, "Live long and prosper, %s. You have successfully beamed aboard!" % name)
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """Render reg page and creates Profile for User afterwards """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                """ Next line of code, automatically creates Profile
                     for user after valid registration"""
                Profile.objects.create(user=request.user)
                name = request.user.username
                messages.success(request, "Live long and prosper, %s. You have successfully beamed aboard!" % name)
                return redirect(reverse('index'))
                # When User registers, a new profile wil be made.
            else:
                messages.error(request, "Unable to register your account at this time!")

    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


@login_required
def user_profile(request, id):
    """ Users profile page"""
    user = User.objects.get(pk=id)
    return render(request, 'profile.html', {"profile": user}, )


@login_required
def edit_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    if profile.user.username != request.user.username:
        return redirect("index")
    else:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, id, instance=profile)

            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                messages.success(request, "You have successfuly edited your Profile!")
                return redirect(user_profile, profile.id)        
        else:
            form = ProfileForm(instance=profile)
    return render(request, 'profileform.html', {'form': form}, {'profile': profile})


@login_required
def user_orders(request):
    orders = Order.objects.filter().order_by('-date')
    return render(request, 'orders.html', {'orders': orders})


@login_required
def inbox(request):
    message = Message.objects.filter().order_by('-created_date')
    return render(request, 'inbox.html', {'message': message})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, "message.html", {'message': message})


@login_required
def create_message(request, id, pk=None):
    message = get_object_or_404(Message, pk=pk) if pk else None
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver_id = id
            message.save()
            messages.success(request, "You have successfuly sent a message!")
            return redirect(message_detail, message.pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'messageform.html', {'form': form})


@login_required
def send_reply(request, pk):
    message = get_object_or_404(Message, pk=pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.message = message
        reply.user = request.user
        reply.profile_id = request.user.id
        reply.save()
        messages.success(request, "You have successfuly replied to a message!")
        return redirect('message_detail', pk=message.id)
    return render(request, 'replyform.html', {'form': form}, )
