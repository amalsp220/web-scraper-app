# Web Scraper App for Small Businesses

🔍 A free, easy-to-use web scraping tool that extracts data from websites and downloads it as Excel files.

## 🌟 Live Demo

**Try it now:** https://huggingface.co/spaces/amalsp/web-scraper-app

## ✨ Features

- 📊 Extract tables from any website
- 🔗 Extract links from web pages
- 📥 Download data as Excel (.xlsx) files
- 🆓 Completely free to use
- 🚀 No installation required
- 💼 Perfect for small business data collection

## 🎯 Use Cases

- Market research and competitor analysis
- Product pricing comparison
- Contact information gathering
- Data collection for business reports
- Lead generation

## 🚀 How to Use

1. Visit the app at https://huggingface.co/spaces/amalsp/web-scraper-app
2. Enter the website URL you want to scrape
3. Choose what to extract:
   - **Tables**: Extracts all table data from the page
   - **Links**: Extracts all hyperlinks with their text
4. Click "Extract Data"
5. Your Excel file will download automatically

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Web Scraping**: BeautifulSoup4, Requests
- **Excel Generation**: Pandas, OpenPyXL
- **Frontend**: HTML, CSS, JavaScript
- **Hosting**: Hugging Face Spaces (Free)
- **Containerization**: Docker

## 💡 Example URLs to Try

- Wikipedia pages with tables
- E-commerce product listings
- Directory websites
- Any website with structured data

## 📦 Local Development

### Prerequisites
- Python 3.11+
- Docker (optional)

### Setup

```bash
# Clone the repository
git clone https://github.com/amalsp220/web-scraper-app.git
cd web-scraper-app

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --host 0.0.0.0 --port 7860
```

Visit http://localhost:7860 in your browser.

### Docker

```bash
# Build the image
docker build -t web-scraper-app .

# Run the container
docker run -p 7860:7860 web-scraper-app
```

## 📁 Project Structure

```
web-scraper-app/
├── main.py                 # FastAPI backend
├── static/
│   └── index.html         # Frontend UI
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔒 Privacy & Security

- No data is stored on our servers
- All scraping is done in real-time
- Downloads are generated on-the-fly
- Respects website robots.txt (use responsibly)

## ⚠️ Disclaimer

This tool is for educational and legitimate business purposes only. Always:
- Check website Terms of Service before scraping
- Respect robots.txt files
- Don't overload servers with requests
- Use scraped data ethically and legally

## 📝 License

MIT License - Free to use for personal and commercial projects

## 👨‍💻 Author

**amalsp**
- Hugging Face: [@amalsp](https://huggingface.co/amalsp)
- GitHub: [@amalsp220](https://github.com/amalsp220)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ for small businesses worldwide**
