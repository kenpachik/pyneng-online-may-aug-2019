# -*- coding: utf-8 -*-
'''
������� 5.3
������ ������ ����������� � ������������:
* ���������� � ������ ���������� (access/trunk),
  * ������ ������ �������: 'Enter interface mode (access/trunk): '
* ������ ���������� (��� � �����, ���� Gi0/3)
  * ������ ������ �������: 'Enter interface type and number: '
* ����� VLAN� (��� ������ trunk ����� ��������� ������ VLAN��)
  * ������ ������ �������: 'Enter vlan(s): '
� ����������� �� ���������� ������, �� ����������� ����� ������,
������ ������������ ��������������� ������������ access ��� trunk
(������� ������ ��������� � ������� access_template � trunk_template).
��� ����, ������� ������ ���� ������ interface � ���������� ����� ����������,
� ����� ��������������� ������, � ������� ���������� ����� VLAN� (��� ������ VLAN��).
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
�� ���� ��� ������ ����� ������ ��� ������������� ������� if � ������ for/while.
���� ������� ���������� �������, ����� ���� ����� ������ ������.
������ ���������� �������, ��� ������ ������ access:
$ python task_5_3.py
������� ����� ������ ���������� (access/trunk): access
������� ��� � ����� ����������: Fa0/6
������� ����� ����(��): 3
interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
������ ���������� �������, ��� ������ ������ trunk:
$ python task_5_3.py
������� ����� ������ ���������� (access/trunk): trunk
������� ��� � ����� ����������: Fa0/7
������� ����� ����(��): 2,3,4,5
interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
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
