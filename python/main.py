from server.yock import Call, Yocki
from yocki.yocki_pb2 import CallRequest, CallResponse
import jsonpickle


@Call(fn="SayHello")
def sayHello(request: CallRequest) -> CallResponse:
    print("recv: {}".format(request))
    return CallResponse(Buf="Hello {}, I'm Python".format(request.Arg))


@Call(fn="Eval")
def evalHandle(requset: CallRequest) -> CallResponse:
    return CallResponse(Buf=str(eval(requset.Arg)))


@Call(fn="Exec")
def execHandle(requset: CallRequest) -> CallResponse:
    result = {}
    exec(requset.Arg, globals(), result)
    return CallResponse(Buf=str(jsonpickle.encode(result)))


Yocki.run()
