# Start

python api.py

```
json
{
  "task": "Build a CLI-based Port Scanner",
  "description": "Create a network port scanning tool that functions both as a command-line utility and as a web API. The scanner should detect open ports on specified IP addresses across a defined range, with support for both TCP and UDP protocols. Additionally, implement banner grabbing functionality to identify services running on open ports.",
  "checkpoints": [
    {
      "id": 1,
      "title": "Basic Functionality Check",
      "description": "The scanner should run with required arguments without crashing",
      "command": "python scanner.py --ip 127.0.0.1 --start-port 300 --end-port 457 --tcp"
    },
    {
      "id": 2,
      "title": "Port Detection Accuracy",
      "description": "The scanner should correctly identify open and closed ports",
      "command": "python scanner.py --ip 127.0.0.1 --start-port 50 --end-port 90 --tcp"
    },
    {
      "id": 3,
      "title": "Banner Grabbing Functionality",
      "description": "The `--banner` flag should trigger banner grabbing on open ports",
      "command": "python scanner.py --ip 127.0.0.1 --start-port 80 --end-port 80 --tcp --banner"
    },
    {
      "id": 4,
      "title": "UDP Scanning",
      "description": "Validate UDP handling doesn't crash, even if the result is filtered",
      "command": "python scanner.py --ip 8.8.8.8 --start-port 53 --end-port 53 --udp"
    }
  ],
  "github_link": "https://github.com/navyarathore/port-scanner.git"
}
```