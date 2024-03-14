from App.models import SecurityEvent
import pyshark

def analyze_packet(packet):
    source_ip = packet.ip.src
    destination_ip = packet.ip.dst
    protocol = packet.transport_layer
    payload = packet.tcp.payload if packet.transport_layer == 'TCP' else None
    
cap = pyshark.FileCapture("capture.pcap")

tcp_traffic = cap.filter("tcp")

for packet in tcp_traffic: 
  if packet.haslayer('HTTP'):
      print(f"HTTP Request Method: {packet[packet.transport_layer].http.request_method}")
  print("---")
cap.close()

threat_detected = check_for_threat(packet)

if threat_detected:
    event_type = "Suspicious Packet"
    description = f"Source IP: {source_ip}, Destination IP: {destination_ip}, Protocol: {protocol}"
    SecurityEvent.objects.create(event_type=event_type, description=description)

def check_for_threat(packet):
     if packet.transport_layer == 'TCP':
        if "malware" in str(packet.tcp.payload).lower() or "exploit" in str(packet.tcp.payload).lower():
            return True 
        return False

def generate_alert(event_type, description):
    SecurityEvent.objects.create(event_type=event_type, description=description)