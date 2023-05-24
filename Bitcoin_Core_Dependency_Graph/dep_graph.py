# This file is just to help visualize the dependency graph of the
# Bitcoin Core codebase
# This project is mostly to help me understand Bitcoin and the internet
# in general


import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

# bitcoind.cpp
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

nx.draw_spring(G, with_labels=True)

plt.show()