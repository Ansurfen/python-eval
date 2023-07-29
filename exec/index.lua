return function(code)
    local res = yocki.call("python-eval", "Exec", code)
    return json.decode(res)
end
