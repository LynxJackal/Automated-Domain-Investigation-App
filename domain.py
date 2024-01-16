import streamlit as st
from streamlit.components.v1 import html


def open_pages_with_delay(urls, delay):
    delay_ms = delay * 1000  
    script = """
        <script type="text/javascript">
            var urls = %s;
            var delay = %s;
            var openLink = function(index) {
                if (index >= urls.length) return;
                window.open(urls[index], '_blank');
                setTimeout(function() { openLink(index + 1); }, delay);
            }
            openLink(0);
        </script>
    """ % (urls, delay_ms)
    html(script)

services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    "Certificate Search": "https://crt.sh/?q={}",
    "Domain History": "https://securitytrails.com/domain/{}",
    "Malware Scanning": "https://www.virustotal.com/gui/domain/{}",
    "builtwith.com": "https://builtwith.com/relationships/{}",
    "dnslytics.com": "https://dnslytics.com/domain/{}",
    "spyonweb.com": "https://spyonweb.com/{}",
    "archive.org": "https://web.archive.org/web/*/{}",
    "CrowdTangle": "https://apps.crowdtangle.com/search?q={}&platform=facebook&sortBy=score&sortOrder=desc",
    "host.io": "https://host.io/{}"
}


domain_input = st.text_input("Enter the domain you want to investigate:", "")

file_uploader = st.file_uploader("Upload a .txt file with domains:")

domains = []
if domain_input:
    domains.append(domain_input)

if file_uploader:

    for line in file_uploader:
        line = line.decode("utf-8").strip()
        if line:
            domains.append(line)

all_formatted_urls = []
for domain in domains:
    formatted_urls = [url.format(domain) for url in services.values()]
    all_formatted_urls.extend(formatted_urls)


if st.button('Open All Links') and all_formatted_urls:
    open_pages_with_delay(all_formatted_urls, delay=2)
