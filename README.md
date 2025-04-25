# Waybackurls Scanner

A Python tool to fetch archived URLs from the Wayback Machine for bug bounty reconnaissance.

## Installation
```bash
git clone https://github.com/RamadhanAlfatih/waybackurls-scanner.git
cd waybackurls-scanner
pip install -r requirements.txt
```

## Usage

### Basic Scanning
```bash
python waybackurls.py -d example.com
```

### Save Results to File
```bash
python waybackurls.py -d example.com -o urls.txt
```

### Advanced Options
| Option          | Description                                  | Example                          |
|-----------------|----------------------------------------------|----------------------------------|
| `-d/--domain`   | Target domain (required)                     | `-d example.com`                 |
| `-o/--output`   | Save results to specified file               | `-o urls.txt`                    |
| `--delay`       | Delay between requests (seconds, default: 1) | `--delay 2`                      |

### Example Output
![Progress Bar Demo](https://via.placeholder.com/600x50?text=Scanning+example.com:+100%25+%7C██████████%7C+50/50+%5B00:52<%5D)

### Common Use Cases

1. **Bug Bounty Recon**
```bash
python waybackurls.py -d target.com -o targets.txt
```

2. **Find Hidden Endpoints**
```bash
python waybackurls.py -d target.com | grep "api\|admin"
```

3. **Combine with Other Tools**
```bash
python waybackurls.py -d target.com | nuclei -t ~/nuclei-templates/
```

## Troubleshooting
**Error: "Failed to get page count"**
- The Wayback Machine API might be temporarily unavailable
- Try increasing the delay: `--delay 3`

**Warning: Slow Scanning**
- For large domains (>1000 pages), use `--delay 2` or higher
- Consider running overnight for massive targets

## Ethical Note
- Respect Wayback Machine's servers - use `--delay` for heavy scanning
- Only scan domains you're authorized to test
- Review Wayback Machine's robots.txt: [web.archive.org/robots.txt](https://web.archive.org/robots.txt)

## License
MIT
