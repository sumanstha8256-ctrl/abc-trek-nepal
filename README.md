# ABC Trek in Nepal — Static Production Website

The official, high-performance static website for **ABC Trek in Nepal** (Annapurna Base Camp Trek Specialists).

This website is built with clean, semantic HTML5, modern CSS3 (Custom Properties & Design Tokens), and vanilla JavaScript. It requires **no server backend, no database, and no paid hosting**.

---

## 📁 Repository Structure

```text
ABC Trek Website/
├── index.html                                        # Primary Homepage
├── plan-your-trek.html                               # Interactive 3-step trip builder
├── design-system.html                                # Living styleguide & UI preview
├── 404.html                                          # Branded 404 error page
├── robots.txt                                        # Search engine crawler instructions
├── sitemap.xml                                       # Canonical XML sitemap (24 URLs)
├── .gitignore                                        # Excludes __pycache__, OS & cache files
├── README.md                                         # Documentation & deployment guide
│
├── css/
│   ├── design-system.css                             # Design tokens (colors, typography, spacing)
│   └── components.css                                # Modular UI components (header, megamenu, cards, footer)
│
├── images/
│   └── suman-shrestha.jpg                            # Founder & expedition director photo
│
├── company/
│   ├── about-us.html                                 # Company story & team credentials
│   └── contact.html                                  # Operations base contact & booking form
│
├── guide/
│   └── annapurna-base-camp-trek-ultimate-guide.html  # Comprehensive Annapurna trekking guide
│
├── safety-ethics/
│   └── high-altitude-medical-protocols-evacuation.html # High-altitude safety & evacuation protocols
│
├── treks/
│   ├── index.html                                    # Full 7-category trek directory & filter
│   └── [18 individual trek pages]                    # e.g., 10-day classic, Poon Hill, Circuit, etc.
│
├── docs/                                             # Architectural Documentation
│   ├── DESIGN_SYSTEM.md                              # Complete design system documentation
│   ├── INFORMATION_ARCHITECTURE.md                   # Sitemap & page hierarchy
│   └── STRATEGIC_BLUEPRINT.md                        # Brand positioning & conversion strategy
│
└── scripts/                                          # Portable Automation & Generator Tools
    ├── server.py                                     # Dual-stack local preview server (port 3000)
    ├── build_catalog.py                              # Regenerates treks/index.html catalog
    ├── generate_pages.py                             # HTML templates for trek pages
    ├── run_generation.py                             # Bulk trek generator
    ├── apply_business_details.py                     # Batch phone/WhatsApp updater
    ├── update_business_info.py                       # Batch footer credentials updater
    └── update_menus.py                               # Megamenu synchronizer
```

---

## 🚀 Running Locally

To test and browse the website locally on your computer:

1. Open PowerShell / Command Prompt in this project directory:
   ```bash
   python scripts/server.py
   ```
2. Open your web browser and visit:
   ```text
   http://localhost:3000/
   ```

*(Press `Ctrl + C` in your terminal to stop the server).*

---

## 🌐 How to Deploy Live for Free

Because this website is 100% static, you can host it live completely free using any of the following platforms:

### Option 1: GitHub Pages (Recommended)

1. **Create a GitHub Account**: If you don't already have one, sign up at [github.com](https://github.com/).
2. **Create a New Repository**:
   - Click the **+** icon in the top-right corner &rarr; **New repository**.
   - Name it (e.g. `abc-trek-nepal`).
   - Choose **Public**.
   - Leave "Initialize with README" unchecked.
   - Click **Create repository**.
3. **Upload Your Files**:
   - On the repository page, click **Upload an existing file** (or use Git / GitHub Desktop).
   - Drag and drop all files and folders from this folder into GitHub and commit.
4. **Enable GitHub Pages**:
   - In your repository, go to **Settings** &rarr; **Pages** (in the left sidebar).
   - Under **Build and deployment** &rarr; **Branch**, select `main` (or `master`) and folder `/ (root)`.
   - Click **Save**.
5. **Your site is live!**
   - GitHub will give you a live URL like: `https://<your-username>.github.io/abc-trek-nepal/`.

---

### Option 2: Vercel (Fastest with Instant Preview)

1. Go to [vercel.com](https://vercel.com/) and sign in with your GitHub account.
2. Click **Add New...** &rarr; **Project**.
3. Import your GitHub repository.
4. Keep the default settings (Framework Preset: *Other*, Root Directory: `./`).
5. Click **Deploy**.
6. In ~15 seconds, your site is live with a free SSL certificate at `https://your-project.vercel.app`.

---

### Option 3: Netlify (Drag & Drop)

1. Go to [netlify.com](https://www.netlify.com/) and log in.
2. Go to the **Sites** tab.
3. Simply drag and drop this entire project folder into the "Drag and drop your site output folder here" box.
4. It will immediately publish your website with a live `.netlify.app` URL.

---

## 📬 Enabling the Contact Form (Without a Server)

In [company/contact.html](company/contact.html), the contact form currently uses a mock submit alert. To receive actual booking and inquiry emails directly in your inbox for free:

1. Sign up for free at [Web3Forms](https://web3forms.com/) or [Formspree](https://formspree.io/).
2. Get your free Access Key.
3. In `company/contact.html`, update the `<form>` tag:
   ```html
   <form action="https://api.web3forms.com/submit" method="POST">
     <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
     <!-- remaining inputs remain exactly the same -->
   </form>
   ```
4. Submissions will now arrive straight to your email!

---

## 🏔️ Brand & Expedition Contacts
- **Specialist Operator**: ABC Trek in Nepal
- **Expedition Lead**: Suman Shrestha
- **Direct Phone / WhatsApp**: +977 9818188459
- **Kathmandu Hub**: Budhanilkantha, Kathmandu, Nepal
- **Operations Base**: Lakeside-6, Pokhara, Nepal
