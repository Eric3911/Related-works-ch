# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2024/4/3 23:28

import torch
import torch.nn as nn
import torch.nn.functional as F

class RWKVBlock(nn.Module):
    def __init__(self, embed_size, num_heads, dropout=0.1):
        super(RWKVBlock, self).__init__()
        self.attn = nn.MultiheadAttention(embed_dim=embed_size, num_heads=num_heads, dropout=dropout)
        self.ln1 = nn.LayerNorm(embed_size)
        self.ln2 = nn.LayerNorm(embed_size)
        self.rnn = nn.GRUCell(embed_size, embed_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        # 自注意力机制
        attn_output, _ = self.attn(x, x, x, attn_mask=mask)
        x = self.ln1(x + self.dropout(attn_output))

        # 循环机制
        new_h = x
        for _ in range(2):  # 假设循环两次
            h = self.rnn(new_h)
            x = x + self.dropout(h)
            new_h = h

        # 再次应用LayerNorm
        x = self.ln2(x)
        return x

class RWKVModel(nn.Module):
    def __init__(self, embed_size, num_heads, num_layers, dropout=0.1):
        super(RWKVModel, self).__init__()
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.num_layers = num_layers
        self.layers = nn.ModuleList([RWKVBlock(embed_size, num_heads, dropout) for _ in range(num_layers)])

    def forward(self, x, mask):
        for layer in self.layers:
            x = layer(x, mask)
        return x

# 假设参数设置
embed_size = 256
num_heads = 8
num_layers = 6
dropout = 0.1

# 实例化RWKV模型
model = RWKVModel(embed_size, num_heads, num_layers, dropout)

# 打印模型结构
print(model)