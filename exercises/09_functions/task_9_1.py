# -*- coding: utf-8 -*-
'''
������� 9.1
������� �������, ������� ���������� ������������ ��� access-������.
������� ������� ����� ���������:
- ������� � ������������� ���������-VLAN ������ ����:
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}
- ������ ������������ access-������ � ���� ������ ������ (������ access_mode_template)
������� ������ ���������� ������ ���� ������ � ������ access
� ������������� �� ������ ������� access_mode_template.
� ����� ����� � ������ �� ������ ���� ������� �������� ������.
� ���� ������� ��������� ��� ������� ��� ������� � ���� ������ ���������� ������ ���� ���� �������.
������ ��������� ������ (������� ������ ����� ������� �������� ������ ��� �������� ������):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
��������� ������ ������� �� ������� ������� access_config.
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def generate_access_config(intf_vlan_mapping, access_template):
    '''
    intf_vlan_mapping - ������� � ������������� ���������-VLAN ������ ����:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - ������ ������ ��� ����� � ������ access
    ���������� ������ ���� ������ � ������ access � ������������� �� ������ �������
    '''
