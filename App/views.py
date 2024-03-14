from django.shortcuts import render
from App.models import SecurityEvent
from .capture import capture_packets
from .analysis import analyze_packet

def home(request):
    return render(request, 'home.html')

def security_alerts(request):
    security_events = SecurityEvent.objects.all()
    return render(request, 'security_alerts.html', {'security_events': security_events})

def capture_traffic(request):
    for packet in capture_packets():
        analyze_packet(packet)
    return render(request, 'capture_complete.html')
