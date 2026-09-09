import os
import shutil
import zipfile

def organize():
    base_dir = os.path.abspath('.')
    
    # Define exact production assets
    prod_folders = [
        'company',
        'css',
        'guide',
        'images',
        'js',
        'safety-ethics',
        'team',
        'treks'
    ]
    
    prod_files = [
        'index.html',
        'blog.html',
        'plan-your-trek.html',
        '404.html',
        'robots.txt',
        'sitemap.xml',
        'favicon.ico',
        'vercel.json'
    ]
    
    # Define internal development tools
    internal_items = [
        'scratch',
        'scripts',
        'docs',
        'design-system.html',
        'preview.bat',
        'README.md'
    ]
    
    # 1. Create deploy_package directory
    deploy_dir = os.path.join(base_dir, 'deploy_package')
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir, exist_ok=True)
    
    # Copy production folders to deploy_package
    for folder in prod_folders:
        src = os.path.join(base_dir, folder)
        dst = os.path.join(deploy_dir, folder)
        if os.path.exists(src):
            shutil.copytree(src, dst)
            print(f"Copied folder: {folder} -> deploy_package/{folder}")
            
    # Copy production files to deploy_package
    for f in prod_files:
        src = os.path.join(base_dir, f)
        dst = os.path.join(deploy_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied file: {f} -> deploy_package/{f}")
            
    # 2. Create deploy_package.zip
    zip_path = os.path.join(base_dir, 'deploy_package.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(deploy_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, deploy_dir)
                zipf.write(file_path, rel_path)
    print(f"Created ready-to-upload archive: deploy_package.zip ({os.path.getsize(zip_path)} bytes)")
    
    # 3. Create _internal_tools folder
    tools_dir = os.path.join(base_dir, '_internal_tools')
    os.makedirs(tools_dir, exist_ok=True)
    
    for item in internal_items:
        src = os.path.join(base_dir, item)
        dst = os.path.join(tools_dir, item)
        if os.path.exists(src):
            if os.path.exists(dst):
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                else:
                    os.remove(dst)
            shutil.move(src, dst)
            print(f"Moved internal item: {item} -> _internal_tools/{item}")
            
    # 4. Create an intelligent dev_server.py in _internal_tools and a convenience runner at root
    dev_server_content = '''import http.server
import socketserver
import os
import sys

# Auto-detect website root (whether run from project root or from _internal_tools)
script_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(script_dir) == '_internal_tools':
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
else:
    project_root = script_dir

os.chdir(project_root)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        clean_path = self.path.split('?')[0].split('#')[0]
        local_path = clean_path.lstrip('/')
        qs = self.path[len(clean_path):]

        # 1. If path ends in .html (and not index.html), redirect to clean URL with 308
        if clean_path.endswith('.html') and clean_path != '/index.html':
            redirect_target = clean_path[:-5] + qs
            self.send_response(308)
            self.send_header('Location', redirect_target)
            self.end_headers()
            return

        # 2. If root, serve index.html
        if not local_path:
            return super().do_GET()

        # 3. If exact file or directory exists, serve normally
        if os.path.exists(local_path):
            return super().do_GET()

        # 4. If path + .html exists, serve .html file under clean URL
        if os.path.exists(local_path + '.html'):
            self.path = clean_path + '.html' + qs
            return super().do_GET()

        return super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
        print(f"Clean URL dev server running at http://127.0.0.1:{PORT}/")
        print(f"Serving files from: {project_root}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\\nShutting down server.")
'''
    with open(os.path.join(tools_dir, 'dev_server.py'), 'w', encoding='utf-8') as f:
        f.write(dev_server_content)
        
    # Also keep dev_server.py at root for easy one-command running
    with open(os.path.join(base_dir, 'dev_server.py'), 'w', encoding='utf-8') as f:
        f.write(dev_server_content)
        
    # Update preview.bat in _internal_tools
    preview_bat = '''@echo off
title ABC Trek Website - Local Clean URL Preview
echo ========================================================
echo   Starting Local Preview Server for ABC Trek in Nepal
echo   Clean URLs Enabled (No .html extensions)
echo ========================================================
echo.
echo Opening http://localhost:8080/ in your browser...
echo.
start http://localhost:8080/
python dev_server.py 8080
pause
'''
    with open(os.path.join(tools_dir, 'preview.bat'), 'w', encoding='utf-8') as f:
        f.write(preview_bat)

    # 5. Update .gitignore
    gitignore_path = os.path.join(base_dir, '.gitignore')
    gitignore_content = '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Caches and logs
*.log
.cache/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
desktop.ini

# Editor & IDE settings
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Internal development tools & deploy bundles
_internal_tools/
deploy_package/
deploy_package.zip
organize_and_package.py
'''
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("Updated .gitignore with _internal_tools, deploy_package, and deploy_package.zip")

    print("\nSUCCESS: Organization and packaging complete!")

if __name__ == '__main__':
    organize()
