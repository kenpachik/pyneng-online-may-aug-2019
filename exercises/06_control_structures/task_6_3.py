# -*- coding: utf-8 -*-
'''
������� 6.3
� ������� ������ ��������� ������������ ��� access-������.
������� ����������� ��������� ������������ ��� ������ trunk.
� ������� �������� ����������� ���, ��� VLAN�� ����� ���� �����, � ���� ��������,
��� � ��� ������.
������� � ������������ ������� ����� ����� ������
� ������ (�������) ������� ������ ��������� ��� ������������ ������ VLAN,
������� ���� ������:
	add - VLAN� ���� ����� �������� (������� switchport trunk allowed vlan add 10,20)
	del - VLAN� ���� ������� �� ������ ����������� (������� switchport trunk allowed vlan remove 17)
	only - �� ���������� ������ �������� ������������ ������ ��������� VLAN� (������� switchport trunk allowed vlan 11,30)
������ ��� ������ 0/1, 0/2, 0/4:
- ������������� ������������ �� ������ ������� trunk_template
- � ������ �������� ���� add, del, only
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

fast_int = {
    'access': {
        '0/12': '10',
        '0/14': '11',
        '0/16': '17',
        '0/17': '150'
    },
    'trunk': {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
}

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
