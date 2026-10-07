from django.contrib import admin

from .models import Employee, EmployeeSkill, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "middle_name",
    )


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "skill",
        "level",
    )