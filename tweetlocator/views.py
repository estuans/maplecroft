
from django.views.generic import ListView, View
from django.http.response import HttpResponse
import json

from .models import Tweet
from .tasks import fetch_latest_tweets

class TweetMapView(ListView):
    model = Tweet
    template_name = "map.html"
    context_object_name = "tweets"



class TweetUpdateView(View):

    def get(self,request):
        task_id = request.GET.get('task_id',None)
        if task_id:
            return self.pollTask(task_id)
        else:
            return self.registerTask()

    def registerTask(self):
        task = fetch_latest_tweets.delay()
        return HttpResponse(json.dumps({'task':task.id}),content_type="application/json")

    def pollTask(self,task_id):
        results = fetch_latest_tweets.AsyncResult(task_id)
        if results.ready():
            jresult = json.dumps({"state":results.ready(),"result": results.result})
            return HttpResponse(jresult,content_type="application/json")
        else:
            return HttpResponse(json.dumps({"state":results.ready()}),content_type="application/json")
