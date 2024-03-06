logger = {
  'warn': lambda log: print(f'\033[0;33m{log}\033[m'),
  'error': lambda log: print(f'\033[0;31m{log}\033[m'),
  'success': lambda log: print(f'\033[0;32m{log}\033[m'),
  'break': print('\n')
}
