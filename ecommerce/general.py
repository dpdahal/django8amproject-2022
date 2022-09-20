from .models import Settings


def data_pass_all_templates(request):
    data = {
        'settingData': Settings.objects.last()
    }

    return data
