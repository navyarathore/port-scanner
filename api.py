from flask import Flask, request, jsonify
import uuid
import threading
import os
import json
import socket
import scanner  # our CLI logic above turned into callable functions

app = Flask(__name__)
SCAN_RESULTS = {}

def run_scan(scan_id, ip, start, end, tcp, udp, banner):
    result = []
    for port in range(start, end + 1):
        if tcp:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                res = s.connect_ex((ip, port))
                if res == 0:
                    entry = {"port": port, "protocol": "TCP"}
                    if banner:
                        try:
                            s.send(b"Hello\r\n")
                            data = s.recv(1024).decode().strip()
                            entry["banner"] = data
                        except:
                            entry["banner"] = "N/A"
                    result.append(entry)
                s.close()
            except:
                pass
        if udp:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(1)
                s.sendto(b"Hello", (ip, port))
                s.recvfrom(1024)
                result.append({"port": port, "protocol": "UDP"})
            except:
                pass
    SCAN_RESULTS[scan_id] = result

@app.route("/scan", methods=["POST"])
def start_scan():
    data = request.json
    ip = data.get("ip")
    start = data.get("start_port", 1)
    end = data.get("end_port", 1024)
    tcp = data.get("protocol", "").lower() == "tcp"
    udp = data.get("protocol", "").lower() == "udp"
    banner = data.get("banner", False)

    scan_id = str(uuid.uuid4())
    t = threading.Thread(target=run_scan, args=(scan_id, ip, start, end, tcp, udp, banner))
    t.start()
    return jsonify({"scan_id": scan_id})

@app.route("/result/<scan_id>")
def get_result(scan_id):
    result = SCAN_RESULTS.get(scan_id, [])
    return jsonify(result)

