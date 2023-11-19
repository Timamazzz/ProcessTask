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
        ws = wb.active
        ws.title = 'ExportedData'

        # Write headers and merge cells
        headers = [
            ('LifeSituation', 'A', 'C'),
            ('Service', 'D', 'H'),
            ('Process', 'I', 'X'),
        ]

        for header, start_column, end_column in headers:
            ws[f'{start_column}1'] = header
            ws.merge_cells(f'{start_column}1:{end_column}1')

        # Write the common headers in the second row
        common_headers = [
            'Identifier', 'Name', 'User',
            'Identifier', 'Name', 'Service Type', 'Regulating Act', 'User',
            'Identifier', 'Name', 'Status', 'Internal Client', 'External Client',
            'Responsible Authority', 'Department', 'Digital Format', 'Non-Digital Format',
            'Digital Format Link', 'Client Value', 'Input Data', 'Output Data',
            'Related Processes', 'Group', 'User',
        ]

        for col_num, header in enumerate(common_headers, start=1):
            ws.cell(row=2, column=col_num, value=header)

        # Create a response with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'
        wb.save(response)
        return response

    export_to_excel.short_description = "Экспорт данных выбранной организации в Excel"


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
