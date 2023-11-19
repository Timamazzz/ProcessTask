import openpyxl
from django.contrib import admin
from django.http import HttpResponse

from .models import CustomUser, LifeSituation, Process, Service, Organization
from django.contrib.auth.admin import UserAdmin


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        # Create a new Excel workbook and add a worksheet
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'ExportedData'

        # Add headers to the worksheet
        headers = [
            'LifeSituation Identifier', 'LifeSituation Name', 'LifeSituation User',
            'Service Identifier', 'Service Name', 'Service Type', 'Service Regulating Act', 'Service User',
            'Process Identifier', 'Process Name', 'Process Status', 'Process Internal Client',
            'Process External Client', 'Process Responsible Authority', 'Process Department',
            'Process Digital Format', 'Process Non-Digital Format', 'Process Digital Format Link',
            'Process Client Value', 'Process Input Data', 'Process Output Data',
            'Process Related Processes', 'Process Group', 'Process User'
        ]
        ws.append(headers)

        # Populate the worksheet with data from the selected Organization
        for organization in queryset:
            life_situations = LifeSituation.objects.filter(user__organization=organization)
            services = Service.objects.filter(user__organization=organization)
            processes = Process.objects.filter(user__organization=organization)

            for life_situation in life_situations:
                row_data = [
                    life_situation.identifier, life_situation.name, life_situation.user.email,
                    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                    None,
                    None, None, None, None, None, None
                ]
                ws.append(row_data)

            for service in services:
                row_data = [
                    None, None, None,
                    service.identifier, service.name, service.service_type.value, service.regulating_act,
                    service.user.email,
                    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
                ]
                ws.append(row_data)

                # If there are multiple processes for a service, merge the rows for each column
                processes_for_service = Process.objects.filter(service=service)
                for process in processes_for_service:
                    row_data = [
                        None, None, None,
                        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                        None, None, None, None, None, None
                    ]
                    row_data[9] = process.identifier
                    row_data[10] = process.name
                    row_data[11] = process.status
                    row_data[12] = process.is_internal_client
                    row_data[13] = process.is_external_client
                    row_data[14] = process.responsible_authority
                    row_data[15] = process.department
                    row_data[16] = process.is_digital_format
                    row_data[17] = process.is_non_digital_format
                    row_data[18] = process.digital_format_link
                    row_data[19] = process.client_value
                    row_data[20] = process.input_data
                    row_data[21] = process.output_data
                    row_data[22] = process.related_processes
                    row_data[23] = process.group
                    row_data[24] = process.user.email
                    ws.append(row_data)

        # Create a response with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'
        wb.save(response)
        return response

    export_to_excel.short_description = "Экспортируйте данные выбранной организации в Excel"


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'patronymic', 'organization')
    search_fields = ('email', 'first_name', 'last_name', 'patronymic', 'organization__name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined', 'organization')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'patronymic', 'organization')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    ordering = ('email',)


class LifeSituationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__email')
    list_filter = ('user', 'name')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'regulating_act', 'lifesituation', 'user')
    search_fields = ('name', 'service_type', 'regulating_act', 'user__email')
    list_filter = ('service_type', 'lifesituation', 'user')


class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'service', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority', 'department',
        'is_digital_format', 'is_non_digital_format')
    search_fields = ('name', 'service__name', 'responsible_authority', 'department')
    list_filter = ('status', 'is_internal_client', 'is_external_client', 'is_digital_format', 'is_non_digital_format')

    fieldsets = (
        (None, {'fields': ('name', 'service', 'status', 'identifier')}),
        ('Responsibility', {'fields': ('responsible_authority', 'department')}),
        ('Digital Format', {'fields': ('is_digital_format', 'is_non_digital_format', 'digital_format_link')}),
        ('Data', {'fields': ('client_value', 'input_data', 'output_data', 'related_processes')}),
    )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LifeSituation, LifeSituationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Process, ProcessAdmin)
