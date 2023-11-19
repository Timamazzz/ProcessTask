import openpyxl
from django.contrib import admin
from django.http import HttpResponse

from .models import CustomUser, LifeSituation, Process, Service, Organization
from django.contrib.auth.admin import UserAdmin


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        # Create a new Excel workbook and add worksheets for each model
        wb = openpyxl.Workbook()
        life_situation_ws = wb.create_sheet(title='LifeSituation')
        service_ws = wb.create_sheet(title='Service')
        process_ws = wb.create_sheet(title='Process')

        # Add headers to each worksheet
        life_situation_ws.append(['Name', 'Identifier', 'User'])
        service_ws.append(['Name', 'Service Type', 'Regulating Act', 'Life Situation', 'Identifier', 'User'])
        process_ws.append(['Name', 'Service', 'Status', 'Internal Client', 'External Client',
                           'Responsible Authority', 'Department', 'Digital Format', 'Non-Digital Format',
                           'Digital Format Link', 'Identifier', 'Client Value', 'Input Data', 'Output Data',
                           'Related Processes', 'User', 'Group'])

        # Populate each worksheet with data from the selected Organization
        for organization in queryset:
            life_situations = LifeSituation.objects.filter(user__organization=organization)
            services = Service.objects.filter(user__organization=organization)
            processes = Process.objects.filter(user__organization=organization)

            for life_situation in life_situations:
                life_situation_ws.append([life_situation.name, life_situation.identifier, life_situation.user.email])

            for service in services:
                service_ws.append([service.name, service.service_type, service.regulating_act, service.lifesituation.identifier,
                                   service.identifier, service.user.email])

            for process in processes:
                process_ws.append([process.name, process.service.identifier, process.status, process.is_internal_client,
                                   process.is_external_client, process.responsible_authority, process.department,
                                   process.is_digital_format, process.is_non_digital_format,
                                   process.digital_format_link,
                                   process.identifier, process.client_value, process.input_data, process.output_data,
                                   process.related_processes, process.user.email, process.group])

        # Create a response with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'
        wb.save(response)
        return response

    export_to_excel.short_description = "Export selected organization's data to Excel"


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
