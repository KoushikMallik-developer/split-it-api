from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("description", "amount", "user_paid", "group")
    search_fields = ("description", "user_paid__username", "group__name")
    list_filter = ("group",)


admin.site.register(Expense, ExpenseAdmin)
