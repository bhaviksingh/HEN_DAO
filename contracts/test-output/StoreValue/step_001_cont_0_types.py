import smartpy as sp

tstorage = sp.TRecord(storedValue = sp.TNat).layout("storedValue")
tparameter = sp.TVariant(divide = sp.TRecord(divisor = sp.TNat).layout("divisor"), double = sp.TUnit, replace = sp.TRecord(value = sp.TNat).layout("value")).layout(("divide", ("double", "replace")))
tglobals = { }
tviews = { }
