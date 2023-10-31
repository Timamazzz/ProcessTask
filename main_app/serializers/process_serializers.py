from rest_framework import serializers
from main_app.models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessDataSerializer(ProcessSerializer):
    class Meta:
        model = Process
        fields = ['client_value', 'input_data', 'output_data', 'related_processes']


class ProcessRetrieveSerializer(ProcessSerializer):
    process_data = ProcessDataSerializer(allow_null=True)

    class Meta:
        model = Process
        fields = ['id', 'name', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department', 'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'identifier',
                  'process_data']

    def to_representation(self, instance):
        process_data = {
            'client_value': instance.client_value,
            'input_data': instance.input_data,
            'output_data': instance.output_data,
            'related_processes': instance.related_processes
        }
        data['process_data'] = process_data
        return data


class ProcessCreateSerializer(ProcessSerializer):
    class Meta:
        model = Process
        fields = ['name', 'service', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department', 'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'identifier']


class ProcessUpdateSerializer(ProcessSerializer):
    process_data = ProcessDataSerializer(allow_null=True)

    class Meta:
        model = Process
        fields = ['id', 'name', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department',
                  'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'process_data']

    def update(self, instance, validated_data):
        data_fields = validated_data.pop('process_data', {})
        if data_fields:
            data_serializer = ProcessDataSerializer(instance.process_data, data_fields)
            if data_serializer.is_valid():
                data_serializer.save()
        for field_name, field_value in validated_data.items():
            setattr(instance, field_name, field_value)
        instance.save()
        return super(ProcessUpdateSerializer, self).update(instance, validated_data)
