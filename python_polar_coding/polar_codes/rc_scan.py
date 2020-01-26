from typing import Union

from .base.polar_code import BasicPolarCode
from .decoders.rc_scan_decoder import RCSCANDecoder


class RCSCANPolarCode(BasicPolarCode):
    """Polar code with RC-SCAN decoding algorithm."""
    decoder_class = RCSCANDecoder

    def __init__(self, N: int, K: int,
                 design_snr: float = 0.0,
                 is_systematic: bool = True,
                 mask: Union[str, None] = None,
                 pcc_method: str = BasicPolarCode.BHATTACHARYYA,
                 I: int = 1):
        self.I = I
        super().__init__(N=N, K=K,
                         is_systematic=is_systematic,
                         design_snr=design_snr,
                         mask=mask,
                         pcc_method=pcc_method)

    def get_decoder(self):
        return self.decoder_class(n=self.n, mask=self.mask,
                                  is_systematic=self.is_systematic, I=self.I)

    def to_dict(self):
        d = super().to_dict()
        d.update({'I': self.I})
        return d