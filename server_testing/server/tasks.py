from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def payload():
    return """<script>console.log('hello world');</script>"""