import os
import re

def update_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<div class="footer-section">\s*<h4>Connect</h4>\s*<ul>\s*<li><a href="https://timeuo\.com/"[^>]*>Time Zone\s*Converter</a></li>\s*</ul>)'
    
    replacement = r'''<div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://timeuo.com/" rel="dofollow noopener" target="_blank">Time Zone Converter</a></li>
                        <li><a href="https://gotbookseriesinorder.com" rel="dofollow noopener" target="_blank">got book series in order</a></li>
                        <li><a href="https://dinosaurhas500teeth.com" rel="dofollow noopener" target="_blank">What Dinosaur Has 500 Teeth</a></li>
                        <li><a href="https://drgo.ca" rel="dofollow noopener" target="_blank">Canada Driving School Near Me</a></li>
                        <li><a href="http://printingnumbering.com" rel="dofollow noopener" target="_blank">printing numbering</a></li>
                    </ul>'''

    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    root_dir = '/Users/bizcheers/jan-20-haolingsheng/haolingsheng/'
    updated_files = 0
    
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories like .git
        if '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if update_footer(file_path):
                    updated_files += 1
                    print(f"Updated: {file_path}")

    print(f"\nTotal files updated: {updated_files}")

if __name__ == "__main__":
    main()
