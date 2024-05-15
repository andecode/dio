from  fastapi import  FastAPI

app=  FastAPI(title='workoutApi')

if __name__ == 'main':
    import uvicorn

    unicorv.run('main.app', host='0.0.0.0, log _level='info', reload=True)
