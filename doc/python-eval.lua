-- Copyright The python-eval authors. All rights reserved.
-- Use of this source code is governed by a MIT-style
-- license that can be found in the LICENSE file.

---@meta _

---@class python_eval
local python_eval = {}

---@param code string
---@return string
function python_eval.say_hello(code) end

---@param code string
---@return table
function python_eval.exec(code) end

---@param code string
---@return string
function python_eval.eval(code) end
