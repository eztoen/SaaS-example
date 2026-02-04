import uvicorn

from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from core.base import Base
from core.db_helper import db_helper
from api.auth.handlers import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.async_engine.begin() as conn:
        print('Starting db ...')
        await conn.run_sync(Base.metadata.create_all)
        
    yield
        
    await conn.close()
    print('Db successfully closed')
    
app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)