from django.shortcuts import render, redirect

from users.forms import UserDetails
from .create_group_form import CreateGroupForm
from .models import ExpenseGroup


def group_list(request):
    pass
    # groups = Group.objects.all()
    # return render(request, "dashboard/group_list.html", {"groups": groups})


def group_detail(request, group_id):
    pass
    # group = get_object_or_404(Group, pk=group_id)
    # return render(request, "dashboard/group_detail.html", {"group": group})


def add_user_to_group(request, group_id):
    pass
    # group = get_object_or_404(Group, pk=group_id)
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     # user = get_object_or_404(User, username=username)  # Use the custom user model
    #     # group.members.add(user)
    # return redirect("group-detail", group_id=group_id)


def create_group(request):
    context = {"is_logged_in": request.session.get("is_logged_in")}
    if request.method == "POST":
        response = CreateGroupForm().create_group(request)
        if response.get("errorMessage"):
            context.update(**response)
            return render(request, "dashboard/create_group.html", context=context)
        else:
            return render(request, "dashboard/create_group.html", context=context)
    else:
        return render(request, "dashboard/create_group.html", context=context)


def delete_group(request, id):
    if request.method == "GET":
        ExpenseGroup.objects.filter(id=id.split("=")[1]).delete()
        return redirect("/dashboard")


def user_dashboard(request):
    if request.method == "GET":
        if request.session.get("is_logged_in"):
            user_details = UserDetails(request).fetch()
            if user_details.errorMessage:
                del request.session["is_logged_in"]
                return redirect("/login")
            groups = ExpenseGroup.objects.filter(
                members__icontains=user_details.data.email
            )
            return render(
                request,
                "dashboard/dashboard.html",
                context={
                    "is_logged_in": request.session.get("is_logged_in"),
                    "groups": groups,
                },
            )
        else:
            request.session["is_logged_in"] = False
            return redirect("/login")
