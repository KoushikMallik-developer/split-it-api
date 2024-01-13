from dashboard.models import ExpenseGroup
from dashboard.types import ExportGroupDetails


class GroupUtils:
    def get_group_details(self, group_id):
        if group_id:
            if ExpenseGroup.objects.filter(id=group_id).exists():
                group = ExpenseGroup.objects.get(id=group_id)
                group = ExportGroupDetails(**group.model_to_dict())
                return group
