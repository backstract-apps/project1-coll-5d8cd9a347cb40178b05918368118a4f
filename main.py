from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - project1-coll-5d8cd9a347cb40178b05918368118a4f',debug=False,docs_url='/suspicious-kiran-1212d286c76011efa1930242ac12000571/docs',openapi_url='/suspicious-kiran-1212d286c76011efa1930242ac12000571/openapi.json')

app.include_router(router, prefix='/suspicious-kiran-1212d286c76011efa1930242ac12000571/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()