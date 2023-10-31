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


class ProcessCreateSerializer(ProcessSerializer):
    class Meta:
        model = Process
        fields = ['name', 'service', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department', 'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'identifier']


class ProcessUpdateSerializer(ProcessSerializer):
    process_data = ProcessDataSerializer(allow_null=True)

    class Meta:
        model = Process
        fields = ['id', 'name', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority', 'department',
                  'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'process_data']

    def update(self, instance, validated_data):
        data_fields = validated_data.pop('process_data', {})

        data_serializer = ProcessDataSerializer(instance, data_fields)
        if data_serializer.is_valid():
            data_serializer.save()

        for field_name, field_value in validated_data.items():
            setattr(instance, field_name, field_value)

        instance.save()

        return super(ProcessUpdateSerializer, self).update(instance, validated_data)
