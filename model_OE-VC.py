import torch
import torch.nn as nn
import torch.nn.functional as F


class LinearNorm(torch.nn.Module):
    def __init__(self, in_dim, out_dim, bias=True, w_init_gain='linear'):
        super(LinearNorm, self).__init__()
        self.linear_layer = torch.nn.Linear(in_dim, out_dim, bias=bias)

        torch.nn.init.xavier_uniform_(
            self.linear_layer.weight,
            gain=torch.nn.init.calculate_gain(w_init_gain))

    def forward(self, x):
        return self.linear_layer(x)


class ConvNorm(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=1, stride=1,
                 padding=None, dilation=1, bias=True, w_init_gain='linear'):
        super(ConvNorm, self).__init__()
        if padding is None:
            assert(kernel_size % 2 == 1)
            padding = int(dilation * (kernel_size - 1) / 2)

        self.conv = torch.nn.Conv1d(in_channels, out_channels,
                                    kernel_size=kernel_size, stride=stride,
                                    padding=padding, dilation=dilation,
                                    bias=bias)

        torch.nn.init.xavier_uniform_(
            self.conv.weight, gain=torch.nn.init.calculate_gain(w_init_gain))

    def forward(self, signal):
        conv_signal = self.conv(signal)
        return conv_signal


class Encoder(nn.Module):
    """Encoder module:
    """
    def __init__(self):
        super(Encoder, self).__init__()

        convolutions = []
        for i in range(3):
            conv_layer = nn.Sequential(
                ConvNorm(80 if i == 0 else 128,
                         128,
                         kernel_size=5, stride=1,
                         padding=2,
                         dilation=1, w_init_gain='relu'),
                nn.BatchNorm1d(128))
            convolutions.append(conv_layer)
        self.convolutions = nn.ModuleList(convolutions)

        self.lstm = nn.LSTM(128, 128, 2, batch_first=True, bidirectional=True)

    def forward(self, x):
        x_ = x
        x = x.squeeze(1).transpose(2, 1)

        for conv in self.convolutions:
            x = F.relu(conv(x))
        x = x.transpose(1, 2)

        self.lstm.flatten_parameters()
        outputs, _ = self.lstm(x)

        return outputs


class Decoder(nn.Module):
    """Decoder module:
    """
    def __init__(self):
        super(Decoder, self).__init__()

        self.lstm1 = nn.LSTM(512, 256, 2, batch_first=True, bidirectional=True)

        convolutions = []
        conv_layer1 = nn.Sequential(
            ConvNorm(512,
                     256,
                     kernel_size=5, stride=1,
                     padding=2,
                     dilation=1, w_init_gain='relu'),
            nn.BatchNorm1d(256))
        convolutions.append(conv_layer1)
        conv_layer2 = nn.Sequential(
            ConvNorm(256,
                     128,
                     kernel_size=5, stride=1,
                     padding=2,
                     dilation=1, w_init_gain='relu'),
            nn.BatchNorm1d(128))
        convolutions.append(conv_layer2)
        conv_layer3 = nn.Sequential(
            ConvNorm(128,
                     80,
                     kernel_size=5, stride=1,
                     padding=2,
                     dilation=1, w_init_gain='relu'),
            nn.BatchNorm1d(80))
        convolutions.append(conv_layer3)
        self.convolutions = nn.ModuleList(convolutions)
        # self.linear_projection = LinearNorm(dim_pre, 80)

    def forward(self, x):

        self.lstm1.flatten_parameters()
        x, _ = self.lstm1(x)
        x = x.transpose(1, 2)

        for conv in self.convolutions:
            x = F.relu(conv(x))
        x = x.transpose(1, 2)

        decoder_output = x

        return decoder_output


class Generator(nn.Module):
    """Generator network:
    """
    def __init__(self):
        super(Generator, self).__init__()

        self.encoder = Encoder()
        self.decoder = Decoder()

    def forward(self, x, c_org):

        encoder_outputs = self.encoder(x)

        tmpo = c_org.unsqueeze(1).expand(-1, x.size(1), -1)
        decoder_inputs = torch.cat((encoder_outputs, c_org.unsqueeze(1).expand(-1, x.size(1), -1)), dim=-1)

        mel_outputs = self.decoder(decoder_inputs)

        return mel_outputs


