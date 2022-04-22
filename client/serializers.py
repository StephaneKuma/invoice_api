from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        read_only_fields = (
            'created_at',
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "email",
            "org_number",
            "address1",
            "address2",
            "zipcode",
            "place",
            "country",
            "contact_person",
            "contact_reference",
            "invoices",
        )
