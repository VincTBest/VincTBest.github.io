import os
import datetime
import xml.etree.ElementTree as ET

# Configuration
DOMAIN = input("Enter your website URL (e.g. https://example.com): ").strip()
OUTPUT_FILE = "sitemap.xml"
VALID_EXTENSIONS = (".html", ".htm")

def get_all_html_files(root_dir):
    """Recursively find all HTML files in the current directory."""
    html_files = []
    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                # Build relative path from the root folder
                rel_path = os.path.relpath(os.path.join(folder, file), root_dir)
                # Convert Windows backslashes to URL slashes
                rel_path = rel_path.replace("\\", "/")
                html_files.append(rel_path)
    return html_files


def generate_sitemap(html_files, output_file):
    """Generate sitemap.xml from a list of HTML files."""
    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"
    })

    for file_path in sorted(html_files):
        url_tag = ET.SubElement(urlset, "url")

        loc = ET.SubElement(url_tag, "loc")
        loc.text = f"{DOMAIN}/{file_path}"

        lastmod = ET.SubElement(url_tag, "lastmod")
        lastmod.text = datetime.datetime.now().strftime("%Y-%m-%d")

        changefreq = ET.SubElement(url_tag, "changefreq")
        changefreq.text = "weekly"

        priority = ET.SubElement(url_tag, "priority")
        priority.text = "0.8"

    tree = ET.ElementTree(urlset)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"✅ Sitemap generated successfully: {output_file}")
    print(f"📄 Total pages added: {len(html_files)}")


if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"🔍 Scanning directory: {current_dir}")

    html_files = get_all_html_files(current_dir)
    if not html_files:
        print("⚠️ No HTML files found in this folder!")
    else:
        generate_sitemap(html_files, OUTPUT_FILE)
