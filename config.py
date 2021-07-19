

specificCommonFiles = [
    # DevOps
    "CMakeLists.txt",
    "core/CMakeLists.txt",
    "test/CMakeLists.txt",
    "test/CMakeLists.txt.in",
    ".gitignore",

    #stencil headers
    "core/include/block_info_database/block_info_database.h",
    "core/include/block_info_database/block_record.h",
    "core/include/chain/chain.h",
    "core/include/chain_writer/chain_writer.h",
    "core/include/chain_writer/file_info.h",
    "core/include/chain_writer/undo_block.h",
    "core/include/coin_database/coin.h",
    "core/include/coin_database/coin_database.h",
    "core/include/coin_database/coin_record.h",
    "core/include/coin_database/undo_coin_record.h",
    "core/include/crypto/rathcrypto.h",
    "core/include/db/db.h",
    "core/include/primitives/block.h",
    "core/include/primitives/block_header.h",
    "core/include/primitives/transaction.h",
    "core/include/primitives/transaction_input.h",
    "core/include/primitives/transaction_output.h",
    "core/include/proto/rath.pb.h",
    "core/include/proto/rath.proto",

    #stencil implementation files
    "core/src/block_info_database/block_record.cpp",
    "core/src/chain_writer/file_info.cpp",
    "core/src/chain_writer/undo_block.cpp",
    "core/src/coin_database/coin.cpp",
    "core/src/coin_database/coin_record.cpp",
    "core/src/coin_database/undo_coin_record.cpp",
    "core/src/crypto/rathcrypto.cpp",
    "core/src/db/db.cpp",
    "core/src/primitives/block.cpp",
    "core/src/primitives/block_record.cpp",
    "core/src/primitives/transaction.cpp",
    "core/src/primitives/transaction_input.cpp",
    "core/src/primitives/transaction_output.cpp",
    "core/src/proto/rath.pb.cc",

    #testing files
    "test/block_info_database/CMakeLists.txt",
    "test/block_info_database/main.cpp",
    "test/chain/CMakeLists.txt",
    "test/chain/main.cpp",
    "test/chain_writer/chain_writer_tests.cpp",
    "test/chain_writer/CMakeLists.txt",
    "test/chain_writer/main.cpp",
    "test/coin_database/coin_database_tests.cpp",
    "test/coin_database/CMakeLists.txt",
    "test/coin_database/main.cpp",
    "test/crypto/crypto_tests.cpp",
    "test/crypto/CMakeLists.txt",
    "test/crypto/main.cpp",
    "test/db/db_tests.cpp",
    "test/db/CMakeLists.txt",
    "test/db/main.cpp",
    "test/primitives/primitives_tests.cpp",
    "test/primitives/CMakeLists.txt",
    "test/primitives/main.cpp",
]