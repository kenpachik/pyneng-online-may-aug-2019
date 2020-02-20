# -*- coding: utf-8 -*-
'''
������� 11.1
������� ������� parse_cdp_neighbors, ������� ������������
����� ������� show cdp neighbors.
� ������� ������ ���� ���� �������� command_output, ������� ������� ��� �������� ����� ������� ����� ������� (�� ��� �����).
������� ������ ���������� �������, ������� ��������� ���������� ����� ������������.
��������, ���� ��� �������� ��� ������� ����� �����:
R4>show cdp neighbors
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
������� ������ ������� ����� �������:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
� ������� ���������� ������ ���� �������� ��� ������� ����� ����� � ������. �� ���� ��� Fa0/0, � �� ��� Fa 0/0.
��������� ������ ������� �� ���������� ����� sh_cdp_n_sw1.txt
�����������: ��� ������� ���� ��������� ��������� ������ ���������� ����.
'''