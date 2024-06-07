from datetime import datetime

from python_polar_coding.channels.simple import SimpleBPSKModulationAWGN
from python_polar_coding.polar_codes import SCPolarCodec
from python_polar_coding.simulation import simulation_task


def fast_ssc_simulation():
    code = SCPolarCodec(N=2048, K=1536, design_snr=2.0)
    channel = SimpleBPSKModulationAWGN(fec_rate=code.K/code.N)
    #snr_range = [2.0, 2.5, 4.2]
    snr_range = [4.2]

    results = list()

    for snr in snr_range:
        start = datetime.now()
        result = simulation_task(code=code,
                                 channel=channel,
                                 snr_db=snr,
                                 messages=1)
        end = datetime.now()
        print(f'Experiment took {(end-start).seconds} seconds')
        results.append(result)

    for r in results:
        print(r)


if __name__ == '__main__':
    fast_ssc_simulation()
