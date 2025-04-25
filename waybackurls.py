import requests
import argparse
import time

def get_wayback_urls(domain, delay=1):
    # Fetch the number of pages
    params = {
        'url': f'{domain}/*',
        'showNumPages': 'true'
    }
    try:
        response = requests.get('http://web.archive.org/cdx/search/cdx', params=params)
        response.raise_for_status()
        num_pages = int(response.text.strip())
    except Exception as e:
        raise Exception(f"Failed to get page count: {e}")

    urls = set()
    for page in range(num_pages):
        params_page = {
            'url': f'{domain}/*',
            'output': 'json',
            'page': page
        }
        try:
            response = requests.get('http://web.archive.org/cdx/search/cdx', params=params_page)
            response.raise_for_status()
            data = response.json()
            if not data:
                continue
            # Skip header row
            for entry in data[1:]:
                original_url = entry[2]  # Third field is 'original' URL
                urls.add(original_url)
        except Exception as e:
            print(f"Warning: Error fetching page {page}: {e}")
        # Respect a delay to avoid overwhelming the server
        time.sleep(delay)
    return sorted(urls)

def main():
    parser = argparse.ArgumentParser(description='Fetch Wayback Machine URLs.')
    parser.add_argument('-d', '--domain', required=True, help='Target domain (e.g., example.com)')
    parser.add_argument('-o', '--output', help='Save results to a file')
    parser.add_argument('--delay', type=float, default=1, help='Delay between requests (seconds)')
    args = parser.parse_args()

    try:
        urls = get_wayback_urls(args.domain, args.delay)
        if args.output:
            with open(args.output, 'w') as f:
                for url in urls:
                    f.write(f"{url}\n")
            print(f"Saved {len(urls)} URLs to {args.output}")
        else:
            for url in urls:
                print(url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()