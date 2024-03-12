import pythonping as ping
import time

serverIP = "158.69.224.61"

start = time.time()
response = ping.ping(serverIP, count=1)
end = time.time()
print("RoundTrip: ", response.rtt_avg_ms)
print("Time: ", (end - start)*1000)
print("Difference: ", (end - start)*1000 - response.rtt_avg_ms)

