import http.server
import socketserver
import json
import time
from urllib.parse import urlparse, parse_qs

PORT = 8000

class TimerHandler(http.server.SimpleHTTPRequestHandler):
    start_time = None
    elapsed_time = 0
    timer_running = False
    reset_time = None

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)

        if path == "/start":
            self.handle_start()
        elif path == "/stop":
            self.handle_stop()
        elif path == "/pause":
            self.handle_pause()
        elif path == "/reset":
            self.handle_reset()
        elif path == "/state":
            self.handle_state()
        elif path == "/set-reset-time":
            self.set_reset_time(query)
        else:
            super().do_GET()

    def handle_start(self):
        if not self.timer_running:
            self.start_time = time.time() - self.elapsed_time
            self.timer_running = True
        self.respond_with_time()

    def handle_pause(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            self.start_time = None
            self.timer_running = False
        self.send_response(200)
        self.end_headers()

    def handle_stop(self):
        self.elapsed_time = 0
        self.start_time = None
        self.timer_running = False
        self.send_response(200)
        self.end_headers()

    def handle_reset(self):
        self.elapsed_time = 0
        self.start_time = None
        self.timer_running = False
        self.reset_time = None
        self.send_response(200)
        self.end_headers()

    def handle_state(self):
        current_elapsed_time = 0 if not self.timer_running else time.time() - self.start_time
        hours, remainder = divmod(int(current_elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"

        if self.reset_time and current_elapsed_time >= self.reset_time:
            self.handle_reset()
            time_string = "00:00:00"

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"time": time_string, "running": self.timer_running}).encode())

    def set_reset_time(self, query):
        try:
            self.reset_time = int(query.get("time", [0])[0])
            self.send_response(200)
        except ValueError:
            self.send_response(400)
        self.end_headers()

    def respond_with_time(self):
        current_elapsed_time = 0 if not self.timer_running else time.time() - self.start_time
        hours, remainder = divmod(int(current_elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"time": time_string}).encode())


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), TimerHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        httpd.serve_forever()
