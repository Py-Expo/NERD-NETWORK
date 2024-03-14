import pyshark
from .analysis import analyze_packet

def capture_packets(interface='eth0', bpf_filter='tcp'):
    try:
        # Initialize LiveCapture object for capturing packets
        capture = pyshark.LiveCapture(interface=interface, bpf_filter=bpf_filter)

        # Continuously capture and analyze packets
        for packet in capture.sniff_continuously():
            # Analyze each packet for security threats
            analyze_packet(packet)

    except pyshark.capture.capture.TSharkCrashException as e:
        print("TShark crashed:", e)
        # Handle TShark crash gracefully
    except Exception as e:
        print("An error occurred during packet capture:", e)
        # Handle other exceptions gracefully

# Example usage:
# capture_packets(interface='eth0', bpf_filter='tcp')
