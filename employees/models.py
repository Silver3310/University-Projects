from django.db import models

from django.utils.translation import gettext_lazy as _

JUNIOR = 0
MIDDLE = 1
SENIOR = 2

SALARY = {
    JUNIOR: 2000,
    MIDDLE: 3000,
    SENIOR: 4000,
}


# Salary depends on the position
POSITIONS = (
    (JUNIOR, f'Junior (Salary {SALARY[JUNIOR]})'),
    (MIDDLE, f'Middle (Salary {SALARY[MIDDLE]})'),
    (SENIOR, f'Senior (Salary {SALARY[SENIOR]})'),
)


class Employee(models.Model):
    """A model for employees

    Attributes:
        name (string): the employee's name
        age (int); the employee's age
        position (string): the employee's position
        balance (int): the current amount of money the employee has

    Methods:
        __str__: the method that defines how to show the employee's info
        promote: the method that promotes the employee's position
        demote: the method that demotes the employee's position
        pay_salary: the method that increases the employee's balance
        give_award: the method to give some awards to an employee

    """

    name = models.CharField(
        max_length=30,
        verbose_name=_('Name')
    )
    birthday = models.DateField(
        verbose_name=_('Birthday (YYYY-MM-DD)'),
    )
    position = models.IntegerField(
        choices=POSITIONS,
        default=JUNIOR,
        verbose_name=_('Position'),
    )
    balance = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Balance')
    )

    def __str__(self):
        """the method that returns the information of an employee"""
        return f'{self.name} ({self.position})'

    def pay_salary(self):
        """pay salary"""

        self.balance += SALARY[self.position]
        self.save()
