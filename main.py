from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Blog API")

# 允许跨域（以后前端 Vue/React 要访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发环境先放开，生产再限制
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"ok": True, "service": "blog-api"}
