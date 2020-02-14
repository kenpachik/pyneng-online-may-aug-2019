# -*- coding: utf-8 -*-
'''
������� 9.4a
������ ����� ��, ��� � ������� 9.4, �� ������� convert_config_to_dict ������ ������������ ��� ���� ������� �����������.
��� ����, �� ������������ � ���������� �������� � �������� �����.
������� ������ ���� �������������, � ���������, ���� ��� ����� ������ �������.
���� ������ ����������� ���:
* �� ������� �������� ������ ����� ������� �������,
* � ������� ���������� - ��������
���� ������ ����������� ���:
* ����� ��������� ������� ������ ���� �������,
* � ��������� - ���������.
��� ������ ������ � �������, ������� � ������ ������ ���� �������.
��������� ������ ������� ���� �� ������� ����� config_r1.txt
�������� �������� �� ���������������� ����.
� ��� ���� ������� � ������� ������������, ��������, �������:
* interface Ethernet0/3.100
* router bgp 100
������ ��������� ������� �� ������� interface Ethernet0/3.100:
'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}
������� ������ ������ ������� ����� ���������� � ����� � ����� �������.
���� ��������� �� ���� �������, � ��������� ����������� ������.
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    ������� ��������� ���������� �� � ������� ����� �� ������ ignore.
    command - ������. �������, ������� ���� ���������
    ignore - ������. ������ ����
    ����������
    * True, ���� � ������� ���������� ����� �� ������ ignore
    * False - ���� ���
    '''
    return any(word in command for word in ignore)