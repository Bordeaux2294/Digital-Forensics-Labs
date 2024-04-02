import whois
import builtwith
import requests
import ssl



#def detect_server_technologies(urls):
 #   results = {}
  #  for url in urls:
   #     try:
    #        technologies = builtwith.parse(url)
     #       results[url] = technologies
     #   except Exception as e:
      #      results[url] = {'error': str(e)}
   # return results


# Predefined list of vulnerabilities associated with server technologies
vulnerability_list = {
    "Apache": ["CVE-2019-0211", "CVE-2019-10082"],
    "Nginx": ["CVE-2019-9511", "CVE-2019-9513"],
    "IIS": ["CVE-2017-7269", "CVE-2020-0688"]
}

def lookup(urls):
    potential_targets = []
    for url in urls:
        print(f"Performing WHOIS lookup for {url}...")
        try:
            # WHOIS Lookup
            domain_info = whois.whois(url)
            print(f"Domain: {url}")
            print(f"Organization: {domain_info.get('org', 'N/A')}")
            print(f"Creation Date: {domain_info.get('creation_date', 'N/A')}")
            print(f"Emails: {domain_info.get('emails', 'N/A')}")
            print("-"*40)
            
            # BuiltWith Analysis
            #print(f"Dectecting server technologies for {url}...")
            #techs = detect_server_technologies(urls)
          #  for url, technologies in techs.items():
           #     print(f"Technologies for {url}:")
            #    if 'error' in technologies:
             #       print(f"Error: {technologies['error']}")
              #  else:
               #     for tech, details in technologies.items():
                #        print(f"{tech}: {details}")
               # print()
           # print("-" * 40)
            
            # Cross-reference with vulnerability list
            #for details, tech  in techs:
             #   if detail in vulnerability_list:
              #      print(f"Server Technology: {details}")
               #     print(f"Known Vulnerabilities: {', '.join(/vulnerability_list[techs])}")
                #    print("-" * 40)
                 #   potential_targets.append(url)
                    
        except Exception as e:
            print(f"Error processing {url}: {e}")
            print("-" * 40)
    #return potential_targets

if __name__ == "__main__":
    urls = [
"https://www.smashingmagazine.com",
"https://www.atlasobscura.com",
"https://www.aeon.co",
"https://www.hackernoon.com",
"https://www.itch.io",
"https://www.dribbble.com",
"https://www.behance.net",
"https://www.sitepoint.com",
"https://www.dev.to",
"https://www.indiehackers.com",
"https://www.producthunt.com",
"https://www.figma.com/community",
"https://www.canva.com",
"https://www.medium.com/m/signin",
"https://www.threadless.com",
"https://www.bandcamp.com",
"https://www.500px.com",
"https://www.ravelry.com",
"https://www.goodreads.com",
"https://www.archiveofourown.org",
"https://www.coursera.org",
"https://www.edx.org",
"https://www.khanacademy.org",
"https://www.udemy.com",
"https://www.hackthissite.org/",
"https://querytracker.net/"
    ]
    lookup(urls)
    #potential_targets = perform_whois_and_builtwith(urls)
    #print("Potential vulnerable websites based on analysis:")
    #for target in potential_targets:
     #   print(target)

