from http_methods.http_methods_enum import HttpMethodsEnum
from send.get_request_sender import GetRequestSender
from send.post_request_sender import PostRequestSender

HTTP_METHODS_FUNCS = {
    HttpMethodsEnum.GET.value: lambda request: GetRequestSender(request).send_request(),
    HttpMethodsEnum.POST.value: lambda request: PostRequestSender(request).send_request()
}
