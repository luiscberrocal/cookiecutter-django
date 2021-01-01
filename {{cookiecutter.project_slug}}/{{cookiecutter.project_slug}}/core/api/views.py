from django.http import JsonResponse

import {{ cookiecutter.project_slug }}

def app_data(request):
    version = {{ cookiecutter.project_slug }}.__version__
    data = dict()
    data['version'] = version
    data['name'] = '{{ cookiecutter.project_name }}'
    data['copyright'] = '2021 (c) EMR Consultants'

    return JsonResponse(data)
