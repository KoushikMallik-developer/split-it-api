import json
from typing import Optional

from django.shortcuts import redirect
from pydantic import BaseModel

from dashboard.models import ExpenseGroup
from users.forms import UserDetails


class CreateGroupForm(BaseModel):
    name: Optional[str] = None
    members: Optional[str] = None

    def create_group(self, request):
        if request.POST.get("group_name") and request.POST.get("group_name") != "":
            self.name = request.POST.get("group_name")
        else:
            return {"errorMessage": "Group Name is required"}
        key = "member"
        count = 1
        members = []
        while True:
            current_key = key + str(count)
            if request.POST.get(current_key):
                if request.POST.get(current_key) != "":
                    members.append(request.POST.get(current_key))
                    count += 1
            else:
                break
        if request.session.get("access_token"):
            user_details = UserDetails(request).fetch()
            if user_details.data.email:
                members.append(user_details.data.email)
            else:
                del request.session["is_logged_in"]
                del request.session["access_token"]
                del request.session["refresh_token"]
                return redirect("/login")
        if not len(members) > 1:
            return {"errorMessage": "Atleast 1 member required."}
        self.members = json.dumps(members)
        is_saved = self.save_group()
        if is_saved:
            return {"successMessage": "New group added."}
        return {"errorMessage": "Group could not be saved."}

    def save_group(self) -> bool:
        if self.name and self.members:
            group = ExpenseGroup(**self.model_dump())
            group.save()
            return True
        else:
            return False
