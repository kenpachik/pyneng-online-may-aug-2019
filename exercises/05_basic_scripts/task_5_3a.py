# -*- coding: utf-8 -*-
'''
������� 5.3a
��������� ������ �� ������� 5.3 ����� �������, �����, � ����������� �� ���������� ������,
���������� ������ ������� � ������� � ������ VLAN� ��� ������ VLAN��:
* ��� access: '������� ����� VLAN:'
* ��� trunk: '������� ����������� VLAN�:'
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
�� ���� ��� ������ ����� ������ ��� ������������� ������� if � ������ for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
