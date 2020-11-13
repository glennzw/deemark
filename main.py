from fastapi import FastAPI
import checkdmarc

app = FastAPI()

@app.get("/api/checkdmarc/{domain}")
async def check_domain(domain: str):
    return checkdmarc.check_domains([domain], include_dmarc_tag_descriptions=True)

#if __name__ == "__main__":
#    uvicorn.run(app)