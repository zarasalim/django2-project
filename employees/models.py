from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название навыка",
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
    )

    middle_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Отчество",
    )

    skills = models.ManyToManyField(
        Skill,
        through="EmployeeSkill",
        verbose_name="Навыки",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник",
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name="Навык",
    )

    level = models.PositiveSmallIntegerField(
    validators=[
        MinValueValidator(1),
        MaxValueValidator(10),
    ],
    verbose_name="Уровень",
)

    def __str__(self):
        return f"{self.employee} — {self.skill}: {self.level}/10"