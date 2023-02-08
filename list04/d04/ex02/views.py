from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from .forms import PlainText as PTF
# from .models import PlainText
from datetime import datetime


def index(request: HttpRequest):
    if request.method == 'POST':
        form = PTF(request.POST)
        if form.is_valid():
            # Write to log file
            with open(settings.LOG_FILE, 'a') as log_file:
                log_file.write(f"{datetime.now()} --- {form.cleaned_data['plain_text']}\n")

        # Goes back to the form page
        return redirect('/ex02')
    
    try:
        # Load all the old logs
        with open(settings.LOG_FILE, 'r') as log_file:
            logs = [line for line in log_file.readlines()]
    except:
        logs = []

    # Renders empty form page with the logs
    return render(request, 'ex02/index.html', {'form': PTF(), 'logs': logs})