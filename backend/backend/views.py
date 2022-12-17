from django.http import HttpResponse, JsonResponse
import json, base64, os


def upload(request):
    if request.method == 'POST':
        body_dict = json.loads(request.body.decode('utf-8'))
        code = body_dict.get('code', '')
        file = open('../../Images/'+code[-3:]+'.jpg','wb')
        file.write(base64.b64decode(code[22:]))
        file.close()
        return HttpResponse(code[-3:],status=200)

def segmentation(request):
    if request.method == 'GET':
        path = ''
        count = len(os.walk(path))
        return JsonResponse({'count':count}, status=200)

    
def download(request):
    if request.method == 'POST':
        file = open('../../Images/result.jpg', 'rb')
        imgcode = file.read(10000000)
        file.close()
        return JsonResponse({'code':str(base64.b64encode(imgcode))}, status=200)