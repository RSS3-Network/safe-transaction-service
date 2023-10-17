create_test_data_v1_0_0 = {
    "master_copy": "0xb6029EA3B2c51D09a50B53CA8012FeEB05bDa35A",
    "setup_data": "0xa97ab18a00000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030000000000000000000000006e45d69a383ceca3d54688e833bd0e1388747e6b00000000000000000000000061a0c717d18232711bc788f19c9cd56a43cc88720000000000000000000000007724b234c9099c205f03b458944942bceba134080000000000000000000000000000000000000000000000000000000000000000",
    "data": "0x61b69abd000000000000000000000000b6029ea3b2c51d09a50b53ca8012feeb05bda35a00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000184a97ab18a00000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030000000000000000000000006e45d69a383ceca3d54688e833bd0e1388747e6b00000000000000000000000061a0c717d18232711bc788f19c9cd56a43cc88720000000000000000000000007724b234c9099c205f03b458944942bceba13408000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
}  # Example from Rinkeby
data_decoded_v1_0_0 = {
    "method": "setup",
    "parameters": [
        {
            "name": "_owners",
            "type": "address[]",
            "value": [
                "0x6E45d69a383CECa3d54688e833Bd0e1388747e6B",
                "0x61a0c717d18232711bC788F19C9Cd56a43cc8872",
                "0x7724b234c9099C205F03b458944942bcEBA13408",
            ],
        },
        {"name": "_threshold", "type": "uint256", "value": "1"},
        {
            "name": "to",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "data", "type": "bytes", "value": "0x"},
        {
            "name": "paymentToken",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "payment", "type": "uint256", "value": "0"},
        {
            "name": "paymentReceiver",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
    ],
}

create_test_data_v1_1_1 = {
    "master_copy": "0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F",
    "setup_data": "0xb63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000180000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ac9b6dd409ff10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000300000000000000000000000085c26101f353f38e45c72d414b44972831f07be3000000000000000000000000235518798770d7336c5c4908dd1019457fea43a10000000000000000000000007f63c25665ea7e85500eaeb806e552e651b07b9d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "data": "0x1688f0b900000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f0000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000002cecc9e861200000000000000000000000000000000000000000000000000000000000001c4b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000180000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ac9b6dd409ff10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000300000000000000000000000085c26101f353f38e45c72d414b44972831f07be3000000000000000000000000235518798770d7336c5c4908dd1019457fea43a10000000000000000000000007f63c25665ea7e85500eaeb806e552e651b07b9d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
}
data_decoded_v1_1_1 = {
    "method": "setup",
    "parameters": [
        {
            "name": "_owners",
            "type": "address[]",
            "value": [
                "0x85C26101f353f38E45c72d414b44972831f07BE3",
                "0x235518798770D7336c5c4908dd1019457FEa43a1",
                "0x7F63c25665EA7e85500eAEB806E552e651B07b9d",
            ],
        },
        {"name": "_threshold", "type": "uint256", "value": "1"},
        {
            "name": "to",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "data", "type": "bytes", "value": "0x"},
        {
            "name": "fallbackHandler",
            "type": "address",
            "value": "0xd5D82B6aDDc9027B22dCA772Aa68D5d74cdBdF44",
        },
        {
            "name": "paymentToken",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "payment", "type": "uint256", "value": "3036537000337393"},
        {
            "name": "paymentReceiver",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
    ],
}

create_cpk_test_data = {
    "master_copy": "0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F",
    "setup_data": "0x5714713d000000000000000000000000ff54516a7bc1c1ea952a688e72d5b93a80620074",
    "data": "0x460868ca00000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5fcfe33a586323e7325be6aa6ecd8b4600d232a9037e83c8ece69413b777dabe6500000000000000000000000040a930851bd2e590bd5a5c981b436de25742e9800000000000000000000000005ef44de4b98f2bce0e29c344e7b2fb8f0282a0cf000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000245714713d000000000000000000000000ff54516a7bc1c1ea952a688e72d5b93a8062007400000000000000000000000000000000000000000000000000000000",
}
data_decoded_cpk = None

# Using `createProxyWithNonce` for v1.4.1, example taken from Goerli
create_v1_4_1_test_data = {
    "master_copy": "0x29fcB43b46531BcA003ddC8FCB67FFE91900C762",
    "setup_data": "0xb63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000fd0732dc9e303f09fcef3a7388ad10a83459ec990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c7d289db6238596b5a5dbe2f1df9d29c930f959c00000000000000000000000068bbf2084546ccba3cf2f604736e77b3b2a671600000000000000000000000000000000000000000000000000000000000000000",
    "data": "0x1688f0b900000000000000000000000029fcb43b46531bca003ddc8fcb67ffe91900c76200000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000018a765221620000000000000000000000000000000000000000000000000000000000000184b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000fd0732dc9e303f09fcef3a7388ad10a83459ec990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c7d289db6238596b5a5dbe2f1df9d29c930f959c00000000000000000000000068bbf2084546ccba3cf2f604736e77b3b2a67160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
}
data_decoded_v1_4_1 = {
    "method": "setup",
    "parameters": [
        {
            "name": "_owners",
            "type": "address[]",
            "value": [
                "0xC7D289DB6238596B5A5DBE2f1dF9D29C930F959c",
                "0x68bbF2084546ccBA3Cf2F604736e77b3b2a67160",
            ],
        },
        {"name": "_threshold", "type": "uint256", "value": "2"},
        {
            "name": "to",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "data", "type": "bytes", "value": "0x"},
        {
            "name": "fallbackHandler",
            "type": "address",
            "value": "0xfd0732Dc9E303f09fCEf3a7388Ad10A83459Ec99",
        },
        {
            "name": "paymentToken",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
        {"name": "payment", "type": "uint256", "value": "0"},
        {
            "name": "paymentReceiver",
            "type": "address",
            "value": "0x0000000000000000000000000000000000000000",
        },
    ],
}