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
    messages.success(
        request, "I have been – and always shall be – your friend. Live long and prosper!")
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
                messages.success(
                    request, "Live long and prosper, %s. You have successfully beamed aboard!" % name)
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
                Message.objects.create(
                    sender_id=1,
                    receiver=request.user,
                    title="Welcome, %s!" % name,
                    message="Welcome, %s, to my Star Trek website. I'm glad you decided to join our community. You have plenty to do here, you can read fresh news from Star Trek world, find something for youself or friends in our Shop, see all the games about Star Trek and join discussions on our forum where you can meet people who like Star Trek as much as you do! Next step is to customize your profile. If you have any questions, just ask. Live long and prosper!" % name)
                messages.success(
                    request, "Live long and prosper, %s. You have successfully beamed aboard! Check your messages and customize your profile. I hope you enjoy your time here!" % name)
                return redirect(reverse('index'))
                # When User registers, a new profile wil be made.
            else:
                messages.error(
                    request, "Unable to register your account at this time!")

    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


@login_required
def user_profile(request, id, pk=None):
    """ Users profile page"""
    user = User.objects.get(pk=id)
    message = get_object_or_404(Message, pk=pk) if pk else None
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver_id = id
            message.save()
            messages.success(request, "You have successfuly sent a message! You can check it in Account > Messages > Outbox.")
            return redirect(user_profile, user.id)
    else:
        form = MessageForm(instance=message)
    return render(request, 'profile.html', {"profile": user}, )


@login_required
def edit_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    if profile.id != request.user.id:
        return redirect("index")
    else:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES,
                                id, instance=profile)

            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                messages.success(
                    request, "You have successfuly edited your Profile!")
                return redirect(user_profile, profile.id)
        else:
            form = ProfileForm(instance=profile)
    return render(request, 'profileform.html', {'form': form}, {'profile': profile},)


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'orders.html', {'orders': orders})


@login_required
def inbox(request):
    inbox = Message.objects.filter(
        receiver=request.user).order_by('-created_date')
    return render(request, 'inbox.html', {'inbox': inbox})


@login_required
def outbox(request):
    outbox = Message.objects.filter(
        sender=request.user).order_by('-created_date')
    return render(request, 'outbox.html', {'outbox': outbox})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    form = ReplyForm(request.POST)
    ctx = {'form': form}
    if form.is_valid():
        reply = form.save(commit=False)
        reply.message = message
        reply.user = request.user
        reply.profile_id = request.user.id
        reply.save()
        messages.success(request, "You have successfuly replied to a message!")
        return redirect('message_detail', pk=message.id)
    return render(request, "message.html", {'message': message}, ctx)
