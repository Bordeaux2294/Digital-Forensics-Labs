import builtwith

def detect_server_technologies(urls):
    results = {}
    for url in urls:
        try:
            technologies = builtwith.parse(url)
            results[url] = technologies
        except Exception as e:
            results[url] = {'error': str(e)}
    return results

if __name__ == "__main__":
    urls = [
"https://www.smashingmagazine.com",
"https://www.atlasobscura.com",
"https://www.aeon.co",
"https://www.lobsters.com",
"https://www.hackernoon.com",
"https://www.itch.io",
"https://www.dribbble.com",
"https://www.behance.net",
"https://www.sitepoint.com",
"https://www.dev.to",
"https://www.indiehackers.com",
"https://www.producthunt.com",
"https://www.figma.com/community"
    ]

    technologies_results = detect_server_technologies(urls)
    for url, technologies in technologies_results.items():
        print(f"Technologies for {url}:")
        if 'error' in technologies:
            print(f"Error: {technologies['error']}")
        else:
            for tech, detail in technologies.items():
                print(f"{tech}: {detail}")
        print()

