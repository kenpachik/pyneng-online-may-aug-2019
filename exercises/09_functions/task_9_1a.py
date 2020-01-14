# -*- coding: utf-8 -*-
'''
������� 9.1a
������� ����� ������� �� ������� 9.1.
��������� ������:
* ������ �������������� ��������, ������� ������������ ����� �� �������� port-security
 * ��� ��������� 'psecurity'
 * �� ��������� �������� None
 * ��� ��������� port-security, ��� �������� ���� �������� ������ ������ port-security (��������� � ������ port_security_template)
������� ������ ���������� ������ ���� ������ � ������ access
� ������������� �� ������ ������� access_mode_template � ������� port_security_template, ���� �� ��� �������.
� ����� ����� � ������ �� ������ ���� ������� �������� ������.
��������� ������ ������� �� ������� ������� access_config,
� ���������� ������������ port-security � ���.
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}
