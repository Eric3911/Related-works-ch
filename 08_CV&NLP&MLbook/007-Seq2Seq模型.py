# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2024/4/3 23:21

import torch
import torch.nn as nn
import torch.nn.functional as F

class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, dropout=0.1):
        super(Encoder, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.rnn = nn.LSTM(hidden_size, hidden_size, num_layers, dropout=dropout)
        self.dropout = nn.Dropout(dropout)

    def forward(self, src, src_length):
        embedded = self.dropout(self.embedding(src))
        packed_embedded = nn.utils.rnn.pack_padded_sequence(embedded, src_length, enforce_sorted=False)
        packed_outputs, (hidden, cell) = self.rnn(packed_embedded)
        outputs, _ = nn.utils.rnn.pad_packed_sequence(packed_outputs, batch_first=True)
        return hidden, cell, outputs

class Attention(nn.Module):
    def __init__(self, hidden_size):
        super(Attention, self).__init__()
        self.attn = nn.Linear(hidden_size * 2, 1)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, hidden, encoder_outputs):
        attention_weights = torch.bmm(hidden.unsqueeze(1), encoder_outputs.transpose(1, 2))
        attention_weights = self.softmax(attention_weights)
        attention_applied = torch.bmm(attention_weights.unsqueeze(1), encoder_outputs)
        return attention_applied

class Decoder(nn.Module):
    def __init__(self, output_size, hidden_size, num_layers=1, dropout=0.1):
        super(Decoder, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.rnn = nn.LSTM(hidden_size, hidden_size, num_layers, dropout=dropout)
        self.fc = nn.Linear(hidden_size, output_size)
        self.attention = Attention(hidden_size)

    def forward(self, input, hidden, cell, encoder_outputs):
        input = input.unsqueeze(0)
        embedded = self.dropout(self.embedding(input))
        embedded, (hidden, cell) = self.rnn(embedded, (hidden, cell))
        embedded = embedded.squeeze(0)
        attention_applied = self.attention(hidden, encoder_outputs)
        output = self.fc(embedded + attention_applied)
        return output, hidden, cell

class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder, device):
        super(Seq2Seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.device = device

    def forward(self, src, src_length, trg, teacher_forcing_ratio=0.5):
        trg_len = trg.shape[0]
        hidden, cell, encoder_outputs = self.encoder(src, src_length)
        decoder_input = trg[0].unsqueeze(0)
        decoder_outputs = torch.zeros(trg_len, 1, self.decoder.output_size).to(self.device)
        for t in range(1, trg_len):
            output, hidden, cell = self.decoder(decoder_input, hidden, cell, encoder_outputs)
            decoder_outputs[t] = output
            teacher_force = random.random() < teacher_forcing_ratio
            top1 = output.argmax(1)
            decoder_input = trg[t].unsqueeze(0) if teacher_force else top1
        return decoder_outputs

# 假设输入尺寸和输出尺寸都是10，隐藏层大小为20
input_size = 10
output_size = 10
hidden_size = 20
num_layers = 1
dropout = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

encoder = Encoder(input_size, hidden_size, num_layers, dropout).to(device)
decoder = Decoder(output_size, hidden_size, num_layers, dropout).to(device)
seq2seq_model = Seq2Seq(encoder, decoder, device)

# 打印模型结构
print(seq2seq_model)