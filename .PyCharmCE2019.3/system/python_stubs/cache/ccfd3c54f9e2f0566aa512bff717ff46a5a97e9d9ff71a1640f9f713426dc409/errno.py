# encoding: utf-8
# module errno
# from (built-in)
# by generator 1.147
"""
This module makes available standard errno system symbols.

The value of each symbol is the corresponding integer value,
e.g., on most systems, errno.ENOENT equals the integer 2.

The dictionary errno.errorcode maps numeric codes to symbol names,
e.g., errno.errorcode[2] could be the string 'ENOENT'.

Symbols that are not relevant to the underlying system are not defined.

To map error codes to error messages, use the function os.strerror(),
e.g. os.strerror(2) could return 'No such file or directory'.
"""
# no imports

# Variables with simple values

E2BIG = 7

EACCES = 13
EADDRINUSE = 98
EADDRNOTAVAIL = 99
EADV = 68
EAFNOSUPPORT = 97
EAGAIN = 11
EALREADY = 114

EBADE = 52
EBADF = 9
EBADFD = 77
EBADMSG = 74
EBADR = 53
EBADRQC = 56
EBADSLT = 57
EBFONT = 59
EBUSY = 16

ECHILD = 10
ECHRNG = 44
ECOMM = 70
ECONNABORTED = 103
ECONNREFUSED = 111
ECONNRESET = 104

EDEADLK = 35
EDEADLOCK = 35
EDESTADDRREQ = 89
EDOM = 33
EDOTDOT = 73
EDQUOT = 122

EEXIST = 17

EFAULT = 14
EFBIG = 27

EHOSTDOWN = 112
EHOSTUNREACH = 113

EIDRM = 43
EILSEQ = 84
EINPROGRESS = 115
EINTR = 4
EINVAL = 22
EIO = 5
EISCONN = 106
EISDIR = 21
EISNAM = 120

EL2HLT = 51
EL2NSYNC = 45
EL3HLT = 46
EL3RST = 47
ELIBACC = 79
ELIBBAD = 80
ELIBEXEC = 83
ELIBMAX = 82
ELIBSCN = 81
ELNRNG = 48
ELOOP = 40

EMFILE = 24
EMLINK = 31
EMSGSIZE = 90
EMULTIHOP = 72

ENAMETOOLONG = 36
ENAVAIL = 119
ENETDOWN = 100
ENETRESET = 102
ENETUNREACH = 101
ENFILE = 23
ENOANO = 55
ENOBUFS = 105
ENOCSI = 50
ENODATA = 61
ENODEV = 19
ENOENT = 2
ENOEXEC = 8
ENOLCK = 37
ENOLINK = 67
ENOMEM = 12
ENOMSG = 42
ENONET = 64
ENOPKG = 65
ENOPROTOOPT = 92
ENOSPC = 28
ENOSR = 63
ENOSTR = 60
ENOSYS = 38
ENOTBLK = 15
ENOTCONN = 107
ENOTDIR = 20
ENOTEMPTY = 39
ENOTNAM = 118
ENOTSOCK = 88
ENOTSUP = 95
ENOTTY = 25
ENOTUNIQ = 76
ENXIO = 6

EOPNOTSUPP = 95
EOVERFLOW = 75

EPERM = 1
EPFNOSUPPORT = 96
EPIPE = 32
EPROTO = 71
EPROTONOSUPPORT = 93
EPROTOTYPE = 91

ERANGE = 34
EREMCHG = 78
EREMOTE = 66
EREMOTEIO = 121
ERESTART = 85
EROFS = 30

ESHUTDOWN = 108
ESOCKTNOSUPPORT = 94
ESPIPE = 29
ESRCH = 3
ESRMNT = 69
ESTALE = 116
ESTRPIPE = 86

ETIME = 62
ETIMEDOUT = 110
ETOOMANYREFS = 109
ETXTBSY = 26

EUCLEAN = 117
EUNATCH = 49
EUSERS = 87

EWOULDBLOCK = 11

EXDEV = 18
EXFULL = 54

# no functions
# no classes
# variables with complex values

errorcode = {
    1: 'EPERM',
    2: 'ENOENT',
    3: 'ESRCH',
    4: 'EINTR',
    5: 'EIO',
    6: 'ENXIO',
    7: 'E2BIG',
    8: 'ENOEXEC',
    9: 'EBADF',
    10: 'ECHILD',
    11: 'EAGAIN',
    12: 'ENOMEM',
    13: 'EACCES',
    14: 'EFAULT',
    15: 'ENOTBLK',
    16: 'EBUSY',
    17: 'EEXIST',
    18: 'EXDEV',
    19: 'ENODEV',
    20: 'ENOTDIR',
    21: 'EISDIR',
    22: 'EINVAL',
    23: 'ENFILE',
    24: 'EMFILE',
    25: 'ENOTTY',
    26: 'ETXTBSY',
    27: 'EFBIG',
    28: 'ENOSPC',
    29: 'ESPIPE',
    30: 'EROFS',
    31: 'EMLINK',
    32: 'EPIPE',
    33: 'EDOM',
    34: 'ERANGE',
    35: 'EDEADLOCK',
    36: 'ENAMETOOLONG',
    37: 'ENOLCK',
    38: 'ENOSYS',
    39: 'ENOTEMPTY',
    40: 'ELOOP',
    42: 'ENOMSG',
    43: 'EIDRM',
    44: 'ECHRNG',
    45: 'EL2NSYNC',
    46: 'EL3HLT',
    47: 'EL3RST',
    48: 'ELNRNG',
    49: 'EUNATCH',
    50: 'ENOCSI',
    51: 'EL2HLT',
    52: 'EBADE',
    53: 'EBADR',
    54: 'EXFULL',
    55: 'ENOANO',
    56: 'EBADRQC',
    57: 'EBADSLT',
    59: 'EBFONT',
    60: 'ENOSTR',
    61: 'ENODATA',
    62: 'ETIME',
    63: 'ENOSR',
    64: 'ENONET',
    65: 'ENOPKG',
    66: 'EREMOTE',
    67: 'ENOLINK',
    68: 'EADV',
    69: 'ESRMNT',
    70: 'ECOMM',
    71: 'EPROTO',
    72: 'EMULTIHOP',
    73: 'EDOTDOT',
    74: 'EBADMSG',
    75: 'EOVERFLOW',
    76: 'ENOTUNIQ',
    77: 'EBADFD',
    78: 'EREMCHG',
    79: 'ELIBACC',
    80: 'ELIBBAD',
    81: 'ELIBSCN',
    82: 'ELIBMAX',
    83: 'ELIBEXEC',
    84: 'EILSEQ',
    85: 'ERESTART',
    86: 'ESTRPIPE',
    87: 'EUSERS',
    88: 'ENOTSOCK',
    89: 'EDESTADDRREQ',
    90: 'EMSGSIZE',
    91: 'EPROTOTYPE',
    92: 'ENOPROTOOPT',
    93: 'EPROTONOSUPPORT',
    94: 'ESOCKTNOSUPPORT',
    95: 'ENOTSUP',
    96: 'EPFNOSUPPORT',
    97: 'EAFNOSUPPORT',
    98: 'EADDRINUSE',
    99: 'EADDRNOTAVAIL',
    100: 'ENETDOWN',
    101: 'ENETUNREACH',
    102: 'ENETRESET',
    103: 'ECONNABORTED',
    104: 'ECONNRESET',
    105: 'ENOBUFS',
    106: 'EISCONN',
    107: 'ENOTCONN',
    108: 'ESHUTDOWN',
    109: 'ETOOMANYREFS',
    110: 'ETIMEDOUT',
    111: 'ECONNREFUSED',
    112: 'EHOSTDOWN',
    113: 'EHOSTUNREACH',
    114: 'EALREADY',
    115: 'EINPROGRESS',
    116: 'ESTALE',
    117: 'EUCLEAN',
    118: 'ENOTNAM',
    119: 'ENAVAIL',
    120: 'EISNAM',
    121: 'EREMOTEIO',
    122: 'EDQUOT',
}

