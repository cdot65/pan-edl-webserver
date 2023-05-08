from django.db import models


class EDLEntry(models.Model):
    ENTRY_TYPE_CHOICES = [
        ("IP", "IP Address"),
        ("Domain", "Domain Name"),
    ]

    entry_type = models.CharField(max_length=50, choices=ENTRY_TYPE_CHOICES)
    entry_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entry_value
