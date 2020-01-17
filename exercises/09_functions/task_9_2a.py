# -*- coding: utf-8 -*-
'''
������� 9.2a
������� ����� ������� generate_trunk_config �� ������� 9.2
�������� ������� ����� �������, ����� ��� ���������� �� ������ ������, � �������:
    - �����: ����� �����������, ���� 'FastEthernet0/1'
    - ��������: ������ ������, ������� ���� ��������� �� ���� ����������
��������� ������ ������� �� ������� ������� trunk_config � ������� trunk_mode_template.
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}
