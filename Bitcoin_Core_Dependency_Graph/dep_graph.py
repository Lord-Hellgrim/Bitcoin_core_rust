# This file is just to help visualize the dependency graph of the
# Bitcoin Core codebase
# This project is mostly to help me understand Bitcoin and the internet
# in general


import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
# depedeps = dependencies and their dependencies
############################# bitcoind.cpp depedeps begin ###################################

# bitcoind.cpp
G.add_edge("config/bitcoin-config.h", "bitcoind.cpp")
G.add_edge("chainparams.h", "bitcoind.cpp")
G.add_edge("common/args.h", "bitcoind.cpp")
G.add_edge("common/init.h", "bitcoind.cpp")
G.add_edge("common/url.h", "bitcoind.cpp")
G.add_edge("compat/compat.h", "bitcoind.cpp")
G.add_edge("init.h", "bitcoind.cpp")
G.add_edge("interfaces/chain.h", "bitcoind.cpp")
G.add_edge("interfaces/init.h", "bitcoind.cpp")
G.add_edge("node/context.h", "bitcoind.cpp")
G.add_edge("node/interface_ui.h", "bitcoind.cpp")
G.add_edge("noui.h", "bitcoind.cpp")
G.add_edge("shutdown.h", "bitcoind.cpp")
G.add_edge("util/check.h", "bitcoind.cpp")
G.add_edge("util/exception.h", "bitcoind.cpp")
G.add_edge("util/strencodings.h", "bitcoind.cpp")
G.add_edge("util/syscall_sandbox.h", "bitcoind.cpp")
G.add_edge("util/syserror.h", "bitcoind.cpp")
G.add_edge("util/system.h", "bitcoind.cpp")
G.add_edge("util/threadnames.h", "bitcoind.cpp")
G.add_edge("util/tokenpipe.h", "bitcoind.cpp")
G.add_edge("util/translation.h", "bitcoind.cpp")

# chainparams.h
G.add_edge("kernel/chainparams.h", "chainparams.h")
G.add_edge("consensus/params.h", "chainparams.h")
G.add_edge("netaddress.h", "chainparams.h")
G.add_edge("primitives/block.h", "chainparams.h")
G.add_edge("protocol.h", "chainparams.h")
G.add_edge("util/chaintype.h", "chainparams.h")
G.add_edge("util/hash_type.h", "chainparams.h")
G.add_edge("cstdint", "chainparams.h")
G.add_edge("memory", "chainparams.h")
G.add_edge("string", "chainparams.h")
G.add_edge("unordered_map", "chainparams.h")
G.add_edge("vector", "chainparams.h")

# clientversion.h
G.add_edge("util/macros.h", "clientversion.h")
G.add_edge("config/bitcoin-config.h", "clientversion.h")
G.add_edge("string", "clientversion.h")
G.add_edge("vector", "clientversion.h")

# common/args.h
G.add_edge("compat/compat.h", "common/args.h")
G.add_edge("sync.h", "common/args.h")
G.add_edge("util/chaintype.h", "common/args.h")
G.add_edge("util/fs.h", "common/args.h")
G.add_edge("util/settings.h", "common/args.h")
G.add_edge("iosfwd", "common/args.h")
G.add_edge("list", "common/args.h")
G.add_edge("map", "common/args.h")
G.add_edge("optional", "common/args.h")
G.add_edge("set", "common/args.h")
G.add_edge("stdint.h", "common/args.h")
G.add_edge("string", "common/args.h")
G.add_edge("variant", "common/args.h")
G.add_edge("vector", "common/args.h")

# common/init.h
G.add_edge("util/translation.h", "common/init.h")
G.add_edge("functional", "common/init.h")
G.add_edge("optional", "common/init.h")
G.add_edge("string", "common/init.h")
G.add_edge("vector", "common/init.h")

# common/url.h
G.add_edge("string", "common/url.h")

# common/compat.h
G.add_edge("config/bitcoin-config.h", "common/compat.h")
G.add_edge("winsock2.h", "common/compat.h")
G.add_edge("ws2tcpip.h", "common/compat.h")
G.add_edge("cstdint", "common/compat.h")
G.add_edge("fcntl.h", "common/compat.h")
G.add_edge("sys/mman.h", "common/compat.h")
G.add_edge("sys/select.h", "common/compat.h")
G.add_edge("sys/socket.h", "common/compat.h")
G.add_edge("sys/types.h", "common/compat.h")
G.add_edge("net/if.h", "common/compat.h")
G.add_edge("netinet/in.h", "common/compat.h")
G.add_edge("netinet/tcp.h", "common/compat.h")
G.add_edge("arpa/inet.h", "common/compat.h")
G.add_edge("ifaddrs.h", "common/compat.h")
G.add_edge("limits.h", "common/compat.h")
G.add_edge("netdb.h", "common/compat.h")
G.add_edge("unistd.h", "common/compat.h")
G.add_edge("cerrno", "common/compat.h")
G.add_edge("BaseTsd.h", "common/compat.h")

# init.h
G.add_edge("any", "init.h")
G.add_edge("memory", "init.h")
G.add_edge("string", "init.h")

# "interfaces/chain.h"
G.add_edge("blockfilter.hd", "interfaces/chain.h")
G.add_edge("primitives/transaction.hd", "interfaces/chain.h")
G.add_edge("util/settings.hd", "interfaces/chain.h")
G.add_edge("functionald", "interfaces/chain.h")
G.add_edge("memoryd", "interfaces/chain.h")
G.add_edge("optionald", "interfaces/chain.h")
G.add_edge("stddef.hd", "interfaces/chain.h")
G.add_edge("stdint.hd", "interfaces/chain.h")
G.add_edge("stringd", "interfaces/chain.h")
G.add_edge("vectord", "interfaces/chain.h")

# interfaces/init.h
G.add_edge("interfaces/chain.h", "interfaces/init.h")
G.add_edge("interfaces/echo.h", "interfaces/init.h")
G.add_edge("interfaces/node.h", "interfaces/init.h")
G.add_edge("interfaces/wallet.h", "interfaces/init.h")
G.add_edge("memory", "interfaces/init.h")

# node/context.h
G.add_edge("kernel/context.h", "node/context.h")
G.add_edge("cassert", "node/context.h")
G.add_edge("functional", "node/context.h")
G.add_edge("memory", "node/context.h")
G.add_edge("vector", "node/context.h")

# node/interface_ui.h
G.add_edge("functional", "node/interfaces")
G.add_edge("memory", "node/interfaces")
G.add_edge("string", "node/interfaces")

# noui.h
G.add_edge("string", "noui.h")

# shutdown.h
G.add_edge("util/translation.h", "shutdown.h")

# util/check.h
G.add_edge("attributes.h", "util/check.h")
G.add_edge("stdexcept", "util/check.h")
G.add_edge("string", "util/check.h")
G.add_edge("string_view", "util/check.h")
G.add_edge("utility", "util/check.h")

# util/exception.h
G.add_edge("exception", "util/exception.h")
G.add_edge("string_view", "util/exception.h")

# util/strencodings.h
G.add_edge("span.h", "util/strencodings.h")
G.add_edge("util/string.h", "util/strencodings.h")
G.add_edge("charconv", "util/strencodings.h")
G.add_edge("cstddef", "util/strencodings.h")
G.add_edge("cstdint", "util/strencodings.h")
G.add_edge("limits", "util/strencodings.h")
G.add_edge("optional", "util/strencodings.h")
G.add_edge("string", "util/strencodings.h")
G.add_edge("string_view", "util/strencodings.h")
G.add_edge("system_error", "util/strencodings.h")
G.add_edge("type_traits", "util/strencodings.h")
G.add_edge("vector", "util/strencodings.h")

# util/syscall_sandbox.h
G.add_node("util/syscall_sandbox.h")

# util/syserror.h
G.add_edge("string", "util/syserror.h")

# util/system.h
G.add_edge("config/bitcoin-config.h", "util/system.h")
G.add_edge("compat/assumptions.h", "util/system.h")
G.add_edge("compat/compat.h", "util/system.h")
G.add_edge("any", "util/system.h")
G.add_edge("set", "util/system.h")
G.add_edge("stdint.h", "util/system.h")
G.add_edge("string", "util/system.h")

# util/threadnames.h
G.add_edge("string", "util/threadnames.h")

# util/tokenpipe.h
G.add_edge("cstdint", "util/tokenpipe.h")
G.add_edge("optional", "util/tokenpipe.h")

# util/translation.h
G.add_edge("tinyformat.h", "util/translation.h")
G.add_edge("functional", "util/translation.h")
G.add_edge("string", "util/translation.h")

########################### bitcoind.cpp depedeps end ###############################

########################### addrdb.cpp depedeps begin ##############################

# addrdb.cpp
G.add_edge("addrdb.h", "addrdb.cpp")
G.add_edge("addrman.h", "addrdb.cpp")
G.add_edge("chainparams.h", "addrdb.cpp")
G.add_edge("clientversion.h", "addrdb.cpp")
G.add_edge("common/args.h", "addrdb.cpp")
G.add_edge("cstdint", "addrdb.cpp")
G.add_edge("hash.h", "addrdb.cpp")
G.add_edge("logging.h", "addrdb.cpp")
G.add_edge("logging/timer.h", "addrdb.cpp")
G.add_edge("netbase.h", "addrdb.cpp")
G.add_edge("netgroup.h", "addrdb.cpp")
G.add_edge("random.h", "addrdb.cpp")
G.add_edge("streams.h", "addrdb.cpp")
G.add_edge("tinyformat.h", "addrdb.cpp")
G.add_edge("univalue.h", "addrdb.cpp")
G.add_edge("util/fs.h", "addrdb.cpp")
G.add_edge("util/fs_helpers.h", "addrdb.cpp")
G.add_edge("util/settings.h", "addrdb.cpp")
G.add_edge("util/translation.h", "addrdb.cpp")

# addrdb.h
G.add_edge("net_types.h", "addrdb.h")
G.add_edge("univalue.h", "addrdb.h")
G.add_edge("util/fs.h", "addrdb.h")
G.add_edge("optional", "addrdb.h")
G.add_edge("vector", "addrdb.h")

# addrman.h
G.add_edge("netaddress.h", "addrman.h")
G.add_edge("netgroup.h", "addrman.h")
G.add_edge("protocol.h", "addrman.h")
G.add_edge("streams.h", "addrman.h")
G.add_edge("util/time.h", "addrman.h")
G.add_edge("cstdint", "addrman.h")
G.add_edge("memory", "addrman.h")
G.add_edge("optional", "addrman.h")
G.add_edge("utility", "addrman.h")
G.add_edge("vector", "addrman.h")

# hash.h
G.add_edge("attributes.h", "hash.h")
G.add_edge("crypto/common.h", "hash.h")
G.add_edge("crypto/ripemd160.h", "hash.h")
G.add_edge("crypto/sha256.h", "hash.h")
G.add_edge("prevector.h", "hash.h")
G.add_edge("serialize.h", "hash.h")
G.add_edge("span.h", "hash.h")
G.add_edge("uint256.h", "hash.h")
G.add_edge("version.h", "hash.h")
G.add_edge("string", "hash.h")
G.add_edge("vector", "hash.h")

# logging.h
G.add_edge("threadsafety.h", "logging.h")
G.add_edge("tinyformat.h", "logging.h")
G.add_edge("util/fs.h", "logging.h")
G.add_edge("util/string.h", "logging.h")
G.add_edge("atomic", "logging.h")
G.add_edge("cstdint", "logging.h")
G.add_edge("functional", "logging.h")
G.add_edge("list", "logging.h")
G.add_edge("mutex", "logging.h")
G.add_edge("string", "logging.h")
G.add_edge("unordered_map", "logging.h")
G.add_edge("vector", "logging.h")

# logging/timer.h
G.add_edge("logging.h", "logging/timer.h")
G.add_edge("util/macros.h", "logging/timer.h")
G.add_edge("util/time.h", "logging/timer.h")
G.add_edge("util/types.h", "logging/timer.h")
G.add_edge("chrono", "logging/timer.h")
G.add_edge("optional", "logging/timer.h")
G.add_edge("string", "logging/timer.h")

# netbase.h
G.add_edge("config/bitcoin-config.h", "netbase.h")
G.add_edge("compat/compat.h", "netbase.h")
G.add_edge("netaddress.h", "netbase.h")
G.add_edge("serialize.h", "netbase.h")
G.add_edge("util/sock.h", "netbase.h")
G.add_edge("functional", "netbase.h")
G.add_edge("memory", "netbase.h")
G.add_edge("stdint.h", "netbase.h")
G.add_edge("string", "netbase.h")
G.add_edge("type_traits", "netbase.h")
G.add_edge("vector", "netbase.h")

# netgroup.h
G.add_edge("netaddress.h", "netgroup.h")
G.add_edge("uint256.h", "netgroup.h")
G.add_edge("vector", "netgroup.h")


nx.draw_spring(G, with_labels=True)

plt.show()