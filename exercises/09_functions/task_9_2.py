# -*- coding: utf-8 -*-
'''
������� 9.2
������� ������� generate_trunk_config, ������� ���������� ������������ ��� trunk-������.
� ������� ������ ���� ����� ���������:
- intf_vlan_mapping: ������� ��� �������� ������� � ������������� ���������-VLAN� ������ ����:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ������� ��� �������� ������ ������������ trunk-������ � ���� ������ ������ (������ trunk_mode_template)
������� ������ ���������� ������ ������ � �������������
�� ������ ��������� ������ � ������� trunk_mode_template.
� ����� ����� � ������ �� ������ ���� ������� �������� ������.
��������� ������ ������� �� ������� ������� trunk_config.
������ ��������� ������ (������� ������ ����� ������� �������� ������ ��� �������� ������):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]
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
