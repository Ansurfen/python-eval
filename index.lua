-- Copyright The python-eval authors. All rights reserved.
-- Use of this source code is governed by a MIT-style
-- license that can be found in the LICENSE file.

return {
    say_hello = import("./sayHello/index"),
    eval = import("./eval/index"),
    exec = import("./exec/index")
}
