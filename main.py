from fastapi import FastAPI
import checkdmarc

app = FastAPI()

@app.get("/api/checkdmarc/{domain}")
async def check_domain(domain: str):
    print("[+] Checking " + domain)
    return checkdmarc.check_domains([domain], include_dmarc_tag_descriptions=True)