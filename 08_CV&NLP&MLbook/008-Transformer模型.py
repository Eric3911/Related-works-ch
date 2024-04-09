# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2024/4/3 23:26

import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.head_dim = embed_size // num_heads

        assert (
            self.head_dim * num_heads == embed_size
        ), "Embedding size needs to be divisible by num_heads"

        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_out = nn.Linear(num_heads * self.head_dim, embed_size)

    def forward(self, values, keys, query, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # Split the embedding into self.num_heads different pieces
        values = values.reshape(N, value_len, self.num_heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.num_heads, self.head_dim)
        queries = query.reshape(N, query_len, self.num_heads, self.head_dim)

        values = self.values(values)
        keys = self.keys(keys)
        queries = self.queries(queries)

        # Attention
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))

        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)

        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
            N, query_len, self.num_heads * self.head_dim
        )

        out = self.fc_out(out)
        return out

class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.dropout(F.relu(self.w_1(x)))  # (N, Q, D, H) -> (N, Q, D, H)
        out = self.w_2(out)  # (N, Q, D, H) -> (N, Q, D)
        return out

class EncoderLayer(nn.Module):
    def __init__(self, embed_size, num_heads, d_ff, dropout=0.1):
        super(EncoderLayer, self).__init__()
        self.mha = MultiHeadAttention(embed_size, num_heads)
        self.ffn = PositionwiseFeedForward(embed_size, d_ff, dropout)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        attn = self.mha(x, x, x, mask)
        x = self.dropout(x + attn)  # Residual connection
        x = self.dropout(x + self.ffn(x))  # Residual connection
        return x

class Transformer(nn.Module):
    def __init__(self, embed_size, num_heads, d_ff, num_layers, dropout=0.1):
        super(Transformer, self).__init__()
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.num_layers = num_layers

        self.pos_encoder = PositionalEncoding(embed_size, dropout)
        self.layers = nn.ModuleList(
            [
                EncoderLayer(
                    embed_size, num_heads, d_ff, dropout
                )
                for _ in range(num_layers)
            ]
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        N, seq_len = x.shape
        pos = self.pos_encoder(x)
        out = x
        for layer in self.layers:
            out = layer(out, mask)
        return out

# 假设参数设置
embed_size = 256
num_heads = 8
d_ff = 512
num_layers = 6
dropout = 0.1

# 实例化Transformer模型
model = Transformer(embed_size, num_heads, d_ff, num_layers, dropout)

# 打印模型结构
print(model)