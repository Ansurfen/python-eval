init("python-eval@1.0.0")
---@type python_eval
local python = import("python-eval@1.0.0")
local res = python.exec([[
def calculate_square(n):
    return n ** 2
result = calculate_square(5)
]])
print(res["result"])
print(python.eval("1+2"))
print(python.say_hello("Yock"))
-- unregister_service("python-eval")
