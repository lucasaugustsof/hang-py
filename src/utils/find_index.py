def find_index(_func, _iter):
  idxs = []

  for value in enumerate(_iter):
    is_right = _func(value[1])

    if is_right:
      idxs.append(value[0])

  return idxs
