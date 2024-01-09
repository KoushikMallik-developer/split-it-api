from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm


def group_list(request):
    groups = Group.objects.all()
    return render(request, "dashboard/group_list.html", {"groups": groups})


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, "dashboard/group_detail.html", {"group": group})


def add_user_to_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        username = request.POST.get("username")
        # user = get_object_or_404(User, username=username)  # Use the custom user model
        # group.members.add(user)
    return redirect("group-detail", group_id=group_id)


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("group-list")
    else:
        form = GroupForm()
    return render(request, "dashboard/create_group.html", {"form": form})


def user_dashboard(request):
    if request.method == "GET":
        if request.session.get("is_logged_in"):
            return render(
                request,
                "dashboard/dashboard.html",
                context={"is_logged_in": request.session.get("is_logged_in")},
            )
        else:
            request.session["is_logged_in"] = False
            return redirect("/login")
