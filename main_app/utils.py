import random
import string

from rest_framework.metadata import SimpleMetadata
from collections import OrderedDict
from django.utils.encoding import force_str
from rest_framework import serializers, viewsets

from main_app.models import LifeSituation, Service, Process


class CustomOptionsMetadata(SimpleMetadata):
    def determine_metadata(self, request, view):
        metadata = super().determine_metadata(request, view)

        serializer_list = getattr(view, 'serializer_list', {})

        if serializer_list:
            actions_metadata = {}
            for key, serializer_class in serializer_list.items():
                serializer_instance = serializer_class()
                fields = self.get_serializer_info(serializer_instance)
                actions_metadata[key] = fields
            metadata['actions'] = actions_metadata

        return metadata

    def get_serializer_info(self, serializer):
        fields = OrderedDict([
            (field_name, self.get_field_info(field))
            for field_name, field in serializer.fields.items()
            if not isinstance(field, serializers.HiddenField)
        ])

        if hasattr(serializer, 'child'):
            fields = self.get_serializer_info(serializer.child)

        return fields

    def get_field_info(self, field):
        field_info = OrderedDict()
        field_info['type'] = self.label_lookup[field]
        field_info['required'] = getattr(field, 'required', False)

        attrs = [
            'read_only', 'label', 'help_text',
            'min_length', 'max_length',
            'min_value', 'max_value'
        ]

        for attr in attrs:
            value = getattr(field, attr, None)
            if value is not None and value != '':
                field_info[attr] = force_str(value, strings_only=True)

        if getattr(field, 'child', None):
            field_info['child'] = self.get_field_info(field.child)
        elif getattr(field, 'fields', None):
            field_info['children'] = self.get_serializer_info(field)

        if (not field_info.get('read_only') and
                not isinstance(field, (serializers.RelatedField, serializers.ManyRelatedField)) and
                hasattr(field, 'choices')):
            field_info['choices'] = [
                {
                    'value': choice_value,
                    'display_name': force_str(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info


class CustomModelViewSet(viewsets.ModelViewSet):
    serializer_list = {}
    metadata_class = CustomOptionsMetadata

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_list.get('create', self.serializer_class)
        elif self.action in ['update', 'partial_update']:
            return self.serializer_list.get('update', self.serializer_class)
        return self.serializer_list.get(self.action, self.serializer_class)


def extract_number_after_last_dot(s):
    parts = s.split('.')

    if len(parts) <= 1:
        return None

    last_part = parts[-1]

    try:
        result = int(last_part)
        return result
    except ValueError:
        return None


def generate_life_situation_identifier(user=None):
    life_situation_last = LifeSituation.objects.filter(user__organization=user.organization).order_by('id').last()
    print('life_situation_last', life_situation_last)
    if life_situation_last:
        last_identifier = extract_number_after_last_dot(life_situation_last.identifier)
        new_identifier = last_identifier + 1
    else:
        new_identifier = 1

    identifier = f"{user.organization.code}.{new_identifier}"
    return identifier


def generate_service_identifier(life_situation):
    last_service = Service.objects.filter(lifesituation=life_situation).order_by('id').last()

    if last_service:
        last_identifier = extract_number_after_last_dot(last_service.identifier)
        new_identifier = last_identifier + 1
    else:
        new_identifier = 1

    identifier = f"{life_situation.identifier}.{new_identifier}"
    return identifier


def generate_process_identifier(service):
    last_process = Process.objects.filter(service=service).order_by('id').last()

    if last_process:
        last_identifier = extract_number_after_last_dot(last_process.identifier)
        new_identifier = last_identifier + 1
    else:
        new_identifier = 1

    identifier = f"{service.identifier}.{new_identifier}"
    return identifier
