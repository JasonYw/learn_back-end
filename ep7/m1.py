from django.middleware.common import CommonMiddleware
class Middle1(CommonMiddleware):
    def process_request(self,request):
        print('m1.request')
        #return request #要把request 传递下去 但是process_request django自动传递request
        #不要轻易返回值，因为返回值后中间件不会继续执行了

    def process_response(self,request,response):
        print('m1.response')
        return response #要把reponse 传递下去 交给下一个中间件


class Middle2(CommonMiddleware):
    def process_request(self,request):
        print('m2.request')
        #return request #要把request 传递下去 但是process_request django自动传递request
        #不要轻易返回值，因为返回值后中间件不会继续执行了

    def process_response(self,request,response):
        print('m2.response')
        return response #要把reponse 传递下去 交给下一个中间件