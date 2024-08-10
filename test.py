import os
import requests


def download_file(url, save_dir, filename):
    """Download a file from a URL and save it to a specified directory with the given filename."""
    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Construct the full path where the file will be saved
    file_path = os.path.join(save_dir, filename)

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Write the content to a file
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f'File downloaded and saved to: {file_path}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading the file from {url}: {e}')


def download_files_from_list(url_list, save_dir):
    """Download multiple files from a list of URLs and save them to the specified directory."""
    for url in url_list:
        # Extract filename from the URL
        filename = url.split('/')[-1]
        download_file(url, save_dir, filename)


# Example usage
url_list = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://v.firebog.net/hosts/Easylist.txt',
    'https://v.firebog.net/hosts/Easyprivacy.txt',
    'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt',
    'https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser',
    'https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt',
    'https://blocklistproject.github.io/Lists/ads.txt',
    'https://blocklistproject.github.io/Lists/tracking.txt',
    'https://blocklistproject.github.io/Lists/smart-tv.txt'
]
save_dir = 'adlists'


def main():
    download_files_from_list(url_list, save_dir)


main()
