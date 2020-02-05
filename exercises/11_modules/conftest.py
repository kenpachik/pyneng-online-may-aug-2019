import pytest


@pytest.fixture(scope='session')
def sh_cdp_n_sw1():
    command_output = '''
SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R6           Eth 0/5         121           R S I           2811       Eth 0/1'''
    return command_output
