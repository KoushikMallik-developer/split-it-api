from django.shortcuts import render, redirect

from users.forms import UserDetails
from .create_group_form import GroupForm
from .models import ExpenseGroup
from .utils import GroupUtils


def group_detail(request, group_id):
    context = {"is_logged_in": request.session.get("is_logged_in")}
    group = GroupUtils().get_group_details(request, group_id.split("=")[1])
    context.update(group.model_dump())
    return render(request, "dashboard/group_detail.html", context=context)


def add_user_to_group(request, id):
    if request.method == "POST":
        context = {"is_logged_in": request.session.get("is_logged_in")}
        group_id = id.split("=")[1]
        response_data = GroupForm().add_user(request, group_id)
        if response_data:
            context.update(**response_data)
            group = GroupUtils().get_group_details(request, group_id)
            context.update(**group.model_dump())
            return render(request, "dashboard/group_detail.html", context=context)


def create_group(request):
    context = {"is_logged_in": request.session.get("is_logged_in")}
    if request.method == "POST":
        response = GroupForm().create_group(request)
        if response:
            context.update(**response)
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
