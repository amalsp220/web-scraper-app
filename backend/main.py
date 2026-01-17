from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

app = FastAPI(title="Simple Web Scraper API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapeRequest(BaseModel):
    url: str
    mode: str = "table"

def scrape_table(soup: BeautifulSoup):
    table = soup.find("table")
    if table is None:
        raise HTTPException(status_code=400, detail="No table found on page")

    headers = []
    header_row = table.find("tr")
    if header_row:
        for th in header_row.find_all(["th", "td"]):
            headers.append(th.get_text(strip=True))
    if not headers:
        first_data_row = table.find("tr")
        if not first_data_row:
            raise HTTPException(status_code=400, detail="Empty table")
        cols = len(first_data_row.find_all("td"))
        headers = [f"col_{i+1}" for i in range(cols)]

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all("td")
        if not cells:
            continue
        row = [c.get_text(strip=True) for c in cells]
        if len(row) < len(headers):
            row += [""] * (len(headers) - len(row))
        elif len(row) > len(headers):
            row = row[: len(headers)]
        rows.append(row)

    df = pd.DataFrame(rows, columns=headers)
    return df

def scrape_links(soup: BeautifulSoup):
    links = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href", "")
        if not href:
            continue
        links.append({"text": text, "href": href})
    if not links:
        raise HTTPException(status_code=400, detail="No links found")
    df = pd.DataFrame(links)
    return df

@app.post("/scrape")
def scrape_to_excel(req: ScrapeRequest):
    try:
        resp = requests.get(req.url, timeout=15)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not fetch URL")

    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail=f"Bad status code: {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")

    if req.mode == "table":
        df = scrape_table(soup)
    elif req.mode == "links":
        df = scrape_links(soup)
    else:
        raise HTTPException(status_code=400, detail="Unsupported mode")

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="data")
    output.seek(0)

    headers = {"Content-Disposition": 'attachment; filename="scraped_data.xlsx"'}

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers,
    )
